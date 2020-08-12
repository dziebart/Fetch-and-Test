from sqlalchemy import create_engine

import secrets
import pymongo
import sqlalchemy
import sys
from multiprocessing import Pool


class Master:

    def __init__(self):
        mongo_client = pymongo.MongoClient(
            "mongodb://" + secrets.mongoUsername + ":" + secrets.mongoPassword + "@cloud.nds.rub.de:42200"
                                                                                 "/?authSource=admin")
        self.data_base = self.get_data_base(mongo_client)
        self.bulk_size = 20

    def get_data_base(self, mongo_client):
        test_data_base = mongo_client['randomness-test6']
        randomness_scans = test_data_base['randomness-test6-0']
        return randomness_scans

    def analyze(self):
        scan_entries = self.data_base.find()
        to_analyze = []

        for scan in scan_entries:
            to_analyze.append(scan)
            if len(to_analyze) >= self.bulk_size:
                self.bulk_analysis(to_analyze)
                to_analyze = []

        if len(to_analyze) > 0:
            self.bulk_analysis(to_analyze)
            to_analyze = []

        # Finished.

    def bulk_analysis(self):
        print("Do something")
        # TODO: Create bulk_size threads with one slave for each thread. Execute each slave and wait for
        # TODO: the results and then finally upload the results to new database.

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
