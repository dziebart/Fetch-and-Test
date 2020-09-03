from sqlalchemy import create_engine
import secrets
import pandas
# import matplotlib
# import bokeh
# import seaborn


def process_string(result):
    processed_results = result.split("/")
    return processed_results


engine = create_engine("mysql+mysqlconnector://" + secrets.mySQLUsername + ":"
                       + secrets.mySQLPassword + "@mysql.cs.upb.de/dziebart")

dbConnection = engine.connect()

frame1 = pandas.read_sql("select * from random_mix_previous_results", dbConnection)
frame2 = pandas.read_sql("select * from random_6_previous_results", dbConnection)
frame3 = pandas.read_sql("select * from random_mix_new_results", dbConnection)
frame4 = pandas.read_sql("select * from random_6_new_results", dbConnection)
frame5 = pandas.read_sql("select * from random_mix_misc_results", dbConnection)
frame6 = pandas.read_sql("select * from random_6_misc_results", dbConnection)

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

for index, row in frame1.iterrows():
    hostName = row['host']
    if hostName not in list_of_hosts:
        #print(str(index)+" "+hostName)

        result = row['monoBitResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            monoBitcounter = monoBitcounter+1

        result = row['randomDuplicatesResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            duplicateCounter = duplicateCounter+1

        result = row['frequencyResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            frequencyCounter = frequencyCounter+1

        result = row['runsResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            runsCounter = runsCounter+1

        result = row['longestRunBlockResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            longestRunCounter = longestRunCounter+1

        result = row['fourierResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            fourierCounter = fourierCounter+1

        result = row['templateResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            templateCounter = templateCounter + 1

        result = row['entropyResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            entropyCounter = entropyCounter + 1

        list_of_hosts.add(hostName)


for index, row in frame2.iterrows():
    hostName = row['host']
    if hostName not in list_of_hosts:
        #print(str(index)+" "+hostName)

        result = row['monoBitResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            monoBitcounter = monoBitcounter+1

        result = row['randomDuplicatesResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            duplicateCounter = duplicateCounter+1

        result = row['frequencyResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            frequencyCounter = frequencyCounter+1

        result = row['runsResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            runsCounter = runsCounter+1

        result = row['longestRunBlockResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            longestRunCounter = longestRunCounter+1

        result = row['fourierResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            fourierCounter = fourierCounter+1

        result = row['templateResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            templateCounter = templateCounter + 1

        result = row['entropyResult']
        result_map = process_string(result)
        if "RANDOM" in result_map:
            entropyCounter = entropyCounter + 1

        list_of_hosts.add(hostName)

########################################################################################################################

print("Hosts that failed MONOBIT with RANDOM : "+str(monoBitcounter))
print("Hosts that failed DUPLICATE_TEST with RANDOM: "+str(duplicateCounter))
print("Hosts that failed FREQUENCY_TEST with RANDOM: "+str(frequencyCounter))
print("Hosts that failed RUNS_TEST with RANDOM: "+str(runsCounter))
print("Hosts that failed LONGEST_RUN_TEST with RANDOM: "+str(longestRunCounter))
print("Hosts that failed FOURIER_TEST with RANDOM: "+str(fourierCounter))
print("Hosts that failed TEMPLATE_TEST with RANDOM: "+str(templateCounter))
print("Hosts that failed ENTROPY_TEST with RANDOM: "+str(entropyCounter))
