from sqlalchemy import create_engine, MetaData

import secrets
import pymongo
import sqlalchemy
import sys
import multiprocessing
from slave import FetchSlave
from multiprocessing import Pool


class Master:

    def __init__(self):
        mongo_client = pymongo.MongoClient(
            "mongodb://" + secrets.mongoUsername + ":" + secrets.mongoPassword + "@cloud.nds.rub.de:42200"
                                                                                 "/?authSource=admin")
        self.data_base = self.get_data_base(mongo_client)
        self.bulk_size = 20

    @staticmethod
    def get_data_base(mongo_client):
        test_data_base = mongo_client['randomness-test6']
        randomness_scans = test_data_base['randomness-test6-0']
        return randomness_scans

    def analyze(self):
        scan_entries = self.data_base.find().limit(20)
        to_analyze = []

        for scan in scan_entries:
            to_analyze.append(scan.copy())
            if len(to_analyze) >= self.bulk_size:
                self.bulk_analysis(to_analyze)
                to_analyze = []

        if len(to_analyze) > 0:
            self.bulk_analysis(to_analyze)
        # Finished. After analyze() the script will exit.
        print("Done!")

    def bulk_analysis(self, analyze_list):
        pool = Pool(20)
        result_list = pool.map(self.execute_slave, analyze_list)
        self.write_results_to_mysql(result_list)

    @staticmethod
    def execute_slave(document):
        slave = FetchSlave(document)
        return slave.get_results()

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
                               + secrets.mySQLPassword+"@mysql.cs.upb.de/dziebart",
                               echo=True)
        return engine


def main():
    master = Master()
    master.analyze()


if __name__ == "__main__":
    main()
