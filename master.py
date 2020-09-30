from sqlalchemy import create_engine, MetaData

import secrets
import pymongo
import gc
import logging
import sqlalchemy
import sys
import multiprocessing
from slave import FetchSlave
from duplicate_slave import DuplicateSlave
from multiprocessing import Pool

logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class Master:

    def __init__(self):
        print("Connecting to Database.")
        mongo_client = pymongo.MongoClient(
            "mongodb://" + secrets.mongoUsername + ":" + secrets.mongoPassword + "@cloud.nds.rub.de:42200"
                                                                                 "/?authSource=admin")
        print("Connected!")
        self.data_base = self.get_data_base(mongo_client)
        self.bulk_size = 10

    @staticmethod
    def get_data_base(mongo_client):
        test_data_base = mongo_client['randomness-test6']
        randomness_scans = test_data_base['randomness-test6-0']
        return randomness_scans

    def analyze(self):
        # Only return those hosts with enough data collected
        minimal_length_filter = {'result.report.randomMinimalLengthResult': 'FULFILLED'}
        scan_entries = self.data_base.find(minimal_length_filter)
        to_analyze = []

        for scan in scan_entries:
            to_analyze.append(scan.copy())
            if len(to_analyze) >= self.bulk_size:
                self.bulk_analysis(to_analyze)
                gc.collect()
                to_analyze = []

        if len(to_analyze) > 0:
            self.bulk_analysis(to_analyze)
        # Finished. After analyze() the script will exit.
        print("Done!")

    def analyze_duplicates(self):
        # Only return those hosts with enough data collected
        minimal_length_filter = {'result.report.randomMinimalLengthResult': 'FULFILLED'}
        scan_entries = self.data_base.find(minimal_length_filter)
        to_analyze = []

        print("Beginning Loop.")

        for scan in scan_entries:
            to_analyze.append(scan.copy())
            if len(to_analyze) >= self.bulk_size:
                self.bulk_analysis_duplicates(to_analyze)
                gc.collect()
                to_analyze = []

        if len(to_analyze) > 0:
            self.bulk_analysis_duplicates(to_analyze)
        # Finished. After analyze() the script will exit.
        print("Done!")

    def bulk_analysis_duplicates(self, analyze_list):
        pool = Pool(10)
        result_list = pool.map(self.execute_duplicate_slave, analyze_list)
        pool.terminate()
        self.write_results_to_file(result_list)

    def bulk_analysis(self, analyze_list):
        pool = Pool(10)
        result_list = pool.map(self.execute_slave, analyze_list)
        pool.terminate()
        self.write_results_to_mysql(result_list)

    @staticmethod
    def execute_slave(document):
        slave = FetchSlave(document)
        return slave.get_results()

    @staticmethod
    def execute_duplicate_slave(document):
        slave = DuplicateSlave(document, 16)
        return_array = [slave.host_name, slave.get_results()]
        return return_array

    def write_results_to_file(self, result_list):
        result_file = open("duplicate_host_list.txt", "a")
        for host in result_list:
            if host[1] is True:
                result_file.write(host[0]+"\n")
        result_file.close()

    def write_results_to_mysql(self, stat_results):
        engine = self.connect_to_mysql()
        meta_data = MetaData(bind=engine, reflect=True)

        for stat in stat_results:
            if stat is None:
                continue

            conn = engine.connect()

            inserter_old = stat.generate_mysql_insert_previous_results(meta_data.tables['previous_results'])
            conn.execute(inserter_old)

            inserter_new = stat.generate_mysql_insert_new_results(meta_data.tables['new_results'])
            conn.execute(inserter_new)

            inserter_misc = stat.generate_mysql_insert_misc(meta_data.tables['misc_results'])
            conn.execute(inserter_misc)

            conn.close()

        engine.dispose()


    @staticmethod
    def connect_to_mysql():
        engine = create_engine("mysql+mysqlconnector://"+secrets.mySQLUsername+":"
                               + secrets.mySQLPassword+"@mysql.cs.upb.de/dziebart")
        return engine


def main():
    analysis_mode = "DUPLICATES"
    master = Master()
    if analysis_mode == "DIEHARDER":
        master.analyze()
    if analysis_mode == "DUPLICATES":
        print("Analyzing Duplicates.")
        master.analyze_duplicates()


if __name__ == "__main__":
    main()
