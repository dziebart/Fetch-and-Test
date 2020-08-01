import pymongo
import pprint
import secrets
import time
# import redis
# import matplotlib
# import bokeh
# seaborn

# See https://python-graph-gallery.com/
mongoClient = pymongo.MongoClient("mongodb://"+secrets.mongoUsername+":"+secrets.mongoPassword+"@cloud.nds.rub.de:42200"
                                                                                               "/?authSource=admin")
# redisClient = redis.Redis(host='cloud.nds.rub.de', port=41200, db=0, password=secrets.redisPassword)

# Print if connected to MongoDB
# print(mongoClient.server_info())
# Raises Exception if no answer
# redisClient.ping()

testDataBase = mongoClient['randomness-test6']

randomnessScans = testDataBase['randomness-test6-0']

testFilter = {
    'result.report.supportsSslTls': True,
    'result.report.serverIsAlive': None
}
start = time.time()
print(randomnessScans.estimated_document_count())
print(randomnessScans.count_documents(testFilter))

alreadyScanned = set()

# counter = 0
# for scan in invalidCurveScans.find(testFilter):
#    counter += 1
#    print(counter)
end = time.time()
print("Time taken: "+str(end - start))

print("Iterating over whole database and filling set.")

scanEntries = randomnessScans.find()

for scan in scanEntries:
    # Do Statistical tests here.
    name = scan['scanTarget']['hostname']
    alreadyScanned.add(name)

print("Switching to fetching newest Entry mode.")

while True:
    time.sleep(10)
    scanEntries = randomnessScans.find().limit(50)
    for scan in scanEntries:
        name = scan['scanTarget']['hostname']
        if name not in alreadyScanned:
            print("NEW SCAN PARSED!")
            print("Hostname: "+name)
            print("Processed Scans: "+str(len(alreadyScanned)))
            alreadyScanned.add(name)
