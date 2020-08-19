import pymongo
import secrets

mongoClient = pymongo.MongoClient("mongodb://"+secrets.mongoUsername+":"+secrets.mongoPassword+"@cloud.nds.rub.de:42200"
                                                                                               "/?authSource=admin")
testDataBase = mongoClient['randomness-test-mix']

randomnessScans = testDataBase['randomness-test-mix-0']

test_filter = {
    'result.report.supportsSslTls': True,
    'result.report.serverIsAlive': None
}

scanEntries = randomnessScans.find(test_filter)

list_of_randoms = set()
list_of_duplicates = dict()

for scan in scanEntries:
    random = scan['result']['report']['extractedRandomList']
    hostname = scan['scanTarget']['hostname']

    if random is not None:
        for rand in random:
            random_bytes = rand.get('array')
            if random_bytes not in list_of_randoms:
                list_of_randoms.add(random_bytes)
            else:
                if random_bytes in list_of_duplicates:
                    if hostname not in list_of_duplicates.get(random_bytes):
                        list_of_duplicates.get(random_bytes).append(hostname)
                else:
                    list_of_duplicates[random_bytes] = [hostname]

testDataBase = mongoClient['randomness-test6']

randomnessScans = testDataBase['randomness-test6-0']

test_filter = {
    'result.report.supportsSslTls': True,
    'result.report.serverIsAlive': None
}

scanEntries = randomnessScans.find(test_filter)

for scan in scanEntries:
    random = scan['result']['report']['extractedRandomList']
    hostname = scan['scanTarget']['hostname']

    if random is not None:
        for rand in random:
            random_bytes = rand.get('array')
            if random_bytes not in list_of_randoms:
                list_of_randoms.add(random_bytes)
            else:
                if random_bytes in list_of_duplicates:
                    if hostname not in list_of_duplicates.get(random_bytes):
                        list_of_duplicates.get(random_bytes).append(hostname)
                else:
                    list_of_duplicates[random_bytes] = [hostname]

for random in list_of_duplicates:
    if len(list_of_duplicates[random]) > 1:
        print(random)

print("Done Scanning for duplicates.")

