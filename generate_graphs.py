from sqlalchemy import create_engine
import secrets
import pandas
import numpy
import matplotlib.pyplot as plt
# import bokeh
# import seaborn


def process_string(result):
    processed_results = result.split("/")
    return processed_results


print("Connecting to the database...")

engine = create_engine("mysql+mysqlconnector://" + secrets.mySQLUsername + ":"
                       + secrets.mySQLPassword + "@mysql.cs.upb.de/dziebart")

dbConnection = engine.connect()

print("Connected!")

print("Loading Data...")
frame1 = pandas.read_sql("select * from random_mix_previous_results", dbConnection)
frame2 = pandas.read_sql("select * from random_6_previous_results", dbConnection)
frame3 = pandas.read_sql("select * from random_mix_new_results", dbConnection)
frame4 = pandas.read_sql("select * from random_6_new_results", dbConnection)
frame5 = pandas.read_sql("select * from random_mix_misc_results", dbConnection)
frame6 = pandas.read_sql("select * from random_6_misc_results", dbConnection)
print("Data loaded!")

########################################################################################################################

list_of_hosts = set()

duplicateCounter = 0
monoBitcounter = 0
frequencyCounter = 0
runsCounter = 0
longestRunCounter = 0
fourierCounter = 0
templateCounter = 0
entropyCounter = 0

hostArray = []

print("Processing Data...")

for index, row in frame1.iterrows():
    hostName = row['host']
    if hostName not in list_of_hosts:
        #print(str(index)+" "+hostName)
        currentHost = numpy.empty(8)

        result = row['monoBitResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            monoBitcounter = monoBitcounter+1
            currentHost[0] = 1
        else:
            currentHost[0] = 0

        result = row['randomDuplicatesResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            duplicateCounter = duplicateCounter+1
            currentHost[1] = 1
        else:
            currentHost[1] = 0

        result = row['frequencyResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            frequencyCounter = frequencyCounter+1
            currentHost[2] = 1
        else:
            currentHost[2] = 0

        result = row['runsResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            runsCounter = runsCounter+1
            currentHost[3] = 1
        else:
            currentHost[3] = 0

        result = row['longestRunBlockResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            longestRunCounter = longestRunCounter+1
            currentHost[4] = 1
        else:
            currentHost[4] = 0

        result = row['fourierResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            fourierCounter = fourierCounter+1
            currentHost[5] = 1
        else:
            currentHost[5] = 0

        result = row['templateResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            templateCounter = templateCounter + 1
            currentHost[6] = 1
        else:
            currentHost[6] = 0

        result = row['entropyResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            entropyCounter = entropyCounter + 1
            currentHost[7] = 1
        else:
            currentHost[7] = 0

        list_of_hosts.add(hostName)
        hostArray.append(currentHost)


for index, row in frame2.iterrows():
    hostName = row['host']
    if hostName not in list_of_hosts:
        #print(str(index)+" "+hostName)
        currentHost = numpy.empty(8)

        result = row['monoBitResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            monoBitcounter = monoBitcounter+1
            currentHost[0] = 1
        else:
            currentHost[0] = 0

        result = row['randomDuplicatesResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            duplicateCounter = duplicateCounter+1
            currentHost[1] = 1
        else:
            currentHost[1] = 0

        result = row['frequencyResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            frequencyCounter = frequencyCounter+1
            currentHost[2] = 1
        else:
            currentHost[2] = 0

        result = row['runsResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            runsCounter = runsCounter+1
            currentHost[3] = 1
        else:
            currentHost[3] = 0

        result = row['longestRunBlockResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            longestRunCounter = longestRunCounter+1
            currentHost[4] = 1
        else:
            currentHost[4] = 0

        result = row['fourierResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            fourierCounter = fourierCounter+1
            currentHost[5] = 1
        else:
            currentHost[5] = 0

        result = row['templateResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            templateCounter = templateCounter + 1
            currentHost[6] = 1
        else:
            currentHost[6] = 0

        result = row['entropyResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            entropyCounter = entropyCounter + 1
            currentHost[7] = 1
        else:
            currentHost[7] = 0

        list_of_hosts.add(hostName)
        hostArray.append(currentHost)

########################################################################################################################

print("Data processed!")

host_results = numpy.stack(hostArray, 0)
counter_labels = ["Monobit Test", "Duplicates", "Frequency Test", "Runs Test", "Longest Run Test", "Fourier Test",
                  "Template Test", "Entropy Test"]
counter_array = numpy.array([monoBitcounter, duplicateCounter, frequencyCounter, runsCounter, longestRunCounter,
                             fourierCounter, templateCounter, entropyCounter])

y_pos = numpy.arange(len(counter_array))
plt.bar(y_pos, counter_array, align='center', color='gold')
plt.title("Hosts with failed ServerHello Random")
plt.xlabel("Test")
plt.ylabel("Hosts failing Test")
plt.xticks(y_pos, counter_labels, rotation=45)

for index, value in enumerate(counter_array):
    print("Current:")
    plt.text(index, value, str(value), va='bottom', ha='center')


print("Number of processed Hosts : "+str(len(list_of_hosts)))
print("Hosts that failed MONOBIT with RANDOM : "+str(monoBitcounter))
print("Hosts that failed DUPLICATE_TEST with RANDOM: "+str(duplicateCounter))
print("Hosts that failed FREQUENCY_TEST with RANDOM: "+str(frequencyCounter))
print("Hosts that failed RUNS_TEST with RANDOM: "+str(runsCounter))
print("Hosts that failed LONGEST_RUN_TEST with RANDOM: "+str(longestRunCounter))
print("Hosts that failed FOURIER_TEST with RANDOM: "+str(fourierCounter))
print("Hosts that failed TEMPLATE_TEST with RANDOM: "+str(templateCounter))
print("Hosts that failed ENTROPY_TEST with RANDOM: "+str(entropyCounter))

plt.show()
