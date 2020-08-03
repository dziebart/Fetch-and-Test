import secrets
import pymongo
from multiprocessing import Pool


def main():
    mongo_client = pymongo.MongoClient(
        "mongodb://" + secrets.mongoUsername + ":" + secrets.mongoPassword + "@cloud.nds.rub.de:42200"
                                                                             "/?authSource=admin")
    data_base = getDataBase(mongo_client)
    # Use function to check for this later
    all_hosts_tested = False

    host_list = set()

    while not all_hosts_tested:
        scan_list = fetchBulk(data_base)

        for scan in scan_list:
            name = scan['scanTarget']['hostname']
            if name not in host_list:
                print("Fetched Host: " + name)
                host_list.add(name)


def getDataBase(mongo_client):
    test_data_base = mongo_client['randomness-test6']
    randomness_scans = test_data_base['randomness-test6-0']
    return randomness_scans


def fetchBulk(data_base):
    # Get 20 or so scans which were not already fetched.
    scan_list = data_base.find().limit(50)  # This will always result in the same 50 Hosts, so change this.
    return scan_list


if __name__ == "__main__":
    main()
