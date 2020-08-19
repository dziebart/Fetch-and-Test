import pymongo
import secrets

mongoClient = pymongo.MongoClient("mongodb://"+secrets.mongoUsername+":"+secrets.mongoPassword+"@cloud.nds.rub.de:42200"
                                                                                               "/?authSource=admin")
testDataBase = mongoClient['randomness-test-mix']

randomnessScans = testDataBase['randomness-test-mix-0']

testFilter = {
    'result.report.supportsSslTls': True,
    'result.report.serverIsAlive': None
}

scanEntries = randomnessScans.find()

list_of_randoms = set()
list_of_duplicates = set()

for scan in scanEntries:
    random = scan['result']['report']['extractedRandomList']
    list_of_current_randoms = set()

    if random is not None:
        for rand in random:
            random_bytes = rand.get('array')
            if random_bytes not in list_of_randoms:
                list_of_randoms.add(random_bytes)
            else:
                if random_bytes not in list_of_current_randoms:
                    # Cross host duplicates and not duplicates on this host
                    list_of_duplicates.add(random_bytes)

            list_of_current_randoms.add(random_bytes)

print(str(list_of_duplicates))

