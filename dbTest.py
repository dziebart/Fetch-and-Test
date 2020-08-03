import pymongo
import pprint
import secrets
import time
import base64
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

scanEntries = randomnessScans.find().limit(20)

for scan in scanEntries:
    # Do Statistical tests here.
    # Use subprocess and invoke DIEHARDER with the appropriate tests.
    name = scan['scanTarget']['hostname']
    random = scan['result']['report']['extractedRandomList']
    iv = scan['result']['report']['extractedIVList']
    session_id = scan['result']['report']['extractedSessionIDList']
    minimum_reached = False

    if scan['result']['report']['randomMinimalLengthResult'] == "FULFILLED":
        minimum_reached = True

    random_string = ""
    if random is not None:
        for rand in random:
            random_string = random_string + rand.get('array')
    if iv is not None:
        for rand in iv:
            random_string = random_string + rand.get('array')
    if session_id is not None:
        for rand in session_id:
            random_string = random_string + rand.get('array')
    if random_string is not None and not "" and minimum_reached:
        raw_bytes = base64.b16decode(random_string)
        newFile = open("byteTest.txt", "wb")
        newFile.write(raw_bytes)
        print("MonoBit Results for comparison: "+str(scan['result']['report']['monoBitResult']))
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
