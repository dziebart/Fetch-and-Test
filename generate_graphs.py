from sqlalchemy import create_engine
import secrets
import pandas
import numpy
import matplotlib.pyplot as plt
import itertools
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

old_tests = False

if(old_tests):

    list_of_hosts = set()

    RANDOMduplicateCounter = 0
    RANDOMmonoBitcounter = 0
    RANDOMfrequencyCounter = 0
    RANDOMrunsCounter = 0
    RANDOMlongestRunCounter = 0
    RANDOMfourierCounter = 0
    RANDOMtemplateCounter = 0
    RANDOMentropyCounter = 0

    SESSIONIDduplicateCounter = 0
    SESSIONIDmonoBitcounter = 0
    SESSIONIDfrequencyCounter = 0
    SESSIONIDrunsCounter = 0
    SESSIONIDlongestRunCounter = 0
    SESSIONIDfourierCounter = 0
    SESSIONIDtemplateCounter = 0
    SESSIONIDentropyCounter = 0

    IVduplicateCounter = 0
    IVmonoBitcounter = 0
    IVfrequencyCounter = 0
    IVrunsCounter = 0
    IVlongestRunCounter = 0
    IVfourierCounter = 0
    IVtemplateCounter = 0
    IVentropyCounter = 0

    COMPLETEmonoBitcounter = 0
    COMPLETEfrequencyCounter = 0
    COMPLETErunsCounter = 0
    COMPLETElongestRunCounter = 0
    COMPLETEfourierCounter = 0
    COMPLETEtemplateCounter = 0
    COMPLETEentropyCounter = 0

    hostArray = []


    print("Processing Data...")

    for index, row in frame1.iterrows():
        hostName = row['host']
        if hostName not in list_of_hosts:
            #print(str(index)+" "+hostName)
            currentHost = numpy.empty(8)

            result = row['monoBitResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMmonoBitcounter = RANDOMmonoBitcounter+1
                currentHost[0] = 1
            else:
                currentHost[0] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDmonoBitcounter = SESSIONIDmonoBitcounter+1

            if 'IV' in result_map:
                IVmonoBitcounter = IVmonoBitcounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEmonoBitcounter = COMPLETEmonoBitcounter+1

            result = row['randomDuplicatesResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMduplicateCounter = RANDOMduplicateCounter+1
                currentHost[1] = 1
            else:
                currentHost[1] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDduplicateCounter = SESSIONIDduplicateCounter+1

            if 'IV' in result_map:
                IVduplicateCounter = IVduplicateCounter+1


            result = row['frequencyResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMfrequencyCounter = RANDOMfrequencyCounter+1
                currentHost[2] = 1
            else:
                currentHost[2] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDfrequencyCounter = SESSIONIDfrequencyCounter+1

            if 'IV' in result_map:
                IVfrequencyCounter = IVfrequencyCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEfrequencyCounter = COMPLETEfrequencyCounter+1

            result = row['runsResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMrunsCounter = RANDOMrunsCounter+1
                currentHost[3] = 1
            else:
                currentHost[3] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDrunsCounter = SESSIONIDrunsCounter+1

            if 'IV' in result_map:
                IVrunsCounter = IVrunsCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETErunsCounter = COMPLETErunsCounter+1

            result = row['longestRunBlockResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMlongestRunCounter = RANDOMlongestRunCounter+1
                currentHost[4] = 1
            else:
                currentHost[4] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDlongestRunCounter = SESSIONIDlongestRunCounter+1

            if 'IV' in result_map:
                IVlongestRunCounter = IVlongestRunCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETElongestRunCounter = COMPLETElongestRunCounter+1

            result = row['fourierResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMfourierCounter = RANDOMfourierCounter+1
                currentHost[5] = 1
            else:
                currentHost[5] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDfourierCounter = SESSIONIDfourierCounter+1

            if 'IV' in result_map:
                IVfourierCounter = IVfourierCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEfourierCounter = COMPLETEfourierCounter+1

            result = row['templateResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMtemplateCounter = RANDOMtemplateCounter + 1
                currentHost[6] = 1
            else:
                currentHost[6] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDtemplateCounter = SESSIONIDtemplateCounter+1

            if 'IV' in result_map:
                IVtemplateCounter = IVtemplateCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEtemplateCounter = COMPLETEtemplateCounter+1

            result = row['entropyResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMentropyCounter = RANDOMentropyCounter + 1
                currentHost[7] = 1
            else:
                currentHost[7] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDentropyCounter = SESSIONIDentropyCounter+1

            if 'IV' in result_map:
                IVentropyCounter = IVentropyCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEentropyCounter = COMPLETEentropyCounter+1

            list_of_hosts.add(hostName)
            hostArray.append(currentHost)


    for index, row in frame2.iterrows():
        hostName = row['host']
        if hostName not in list_of_hosts:
            #print(str(index)+" "+hostName)
            currentHost = numpy.empty(8)

            result = row['monoBitResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMmonoBitcounter = RANDOMmonoBitcounter+1
                currentHost[0] = 1
            else:
                currentHost[0] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDmonoBitcounter = SESSIONIDmonoBitcounter+1

            if 'IV' in result_map:
                IVmonoBitcounter = IVmonoBitcounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEmonoBitcounter = COMPLETEmonoBitcounter+1

            result = row['randomDuplicatesResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMduplicateCounter = RANDOMduplicateCounter+1
                currentHost[1] = 1
            else:
                currentHost[1] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDduplicateCounter = SESSIONIDduplicateCounter+1

            if 'IV' in result_map:
                IVduplicateCounter = IVduplicateCounter+1


            result = row['frequencyResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMfrequencyCounter = RANDOMfrequencyCounter+1
                currentHost[2] = 1
            else:
                currentHost[2] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDfrequencyCounter = SESSIONIDfrequencyCounter+1

            if 'IV' in result_map:
                IVfrequencyCounter = IVfrequencyCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEfrequencyCounter = COMPLETEfrequencyCounter+1

            result = row['runsResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMrunsCounter = RANDOMrunsCounter+1
                currentHost[3] = 1
            else:
                currentHost[3] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDrunsCounter = SESSIONIDrunsCounter+1

            if 'IV' in result_map:
                IVrunsCounter = IVrunsCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETErunsCounter = COMPLETErunsCounter+1

            result = row['longestRunBlockResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMlongestRunCounter = RANDOMlongestRunCounter+1
                currentHost[4] = 1
            else:
                currentHost[4] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDlongestRunCounter = SESSIONIDlongestRunCounter+1

            if 'IV' in result_map:
                IVlongestRunCounter = IVlongestRunCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETElongestRunCounter = COMPLETElongestRunCounter+1

            result = row['fourierResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMfourierCounter = RANDOMfourierCounter+1
                currentHost[5] = 1
            else:
                currentHost[5] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDfourierCounter = SESSIONIDfourierCounter+1

            if 'IV' in result_map:
                IVfourierCounter = IVfourierCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEfourierCounter = COMPLETEfourierCounter+1

            result = row['templateResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMtemplateCounter = RANDOMtemplateCounter + 1
                currentHost[6] = 1
            else:
                currentHost[6] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDtemplateCounter = SESSIONIDtemplateCounter+1

            if 'IV' in result_map:
                IVtemplateCounter = IVtemplateCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEtemplateCounter = COMPLETEtemplateCounter+1

            result = row['entropyResult']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMentropyCounter = RANDOMentropyCounter + 1
                currentHost[7] = 1
            else:
                currentHost[7] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDentropyCounter = SESSIONIDentropyCounter+1

            if 'IV' in result_map:
                IVentropyCounter = IVentropyCounter+1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEentropyCounter = COMPLETEentropyCounter+1

            list_of_hosts.add(hostName)
            hostArray.append(currentHost)

    ########################################################################################################################

    print("Data processed!")

    host_results = numpy.stack(hostArray, 0)
    counter_labels = ["Monobit Test", "Duplicates", "Frequency Test", "Runs Test", "Longest Run Test", "Fourier Test",
                      "Template Test", "Entropy Test"]
    counter_labels_without_duplicate = ["Monobit Test", "Frequency Test", "Runs Test", "Longest Run Test", "Fourier Test",
                      "Template Test", "Entropy Test"]

    #FOR COMPLETE SEQUENCE:
    #aggregate_labels = ["All Tests passed", "All Tests failed but no Duplicates", "Only Template Test failed",
    #                    "Template and Entropy Test failed", "Monobit, Template and Entropy Test failed",
    #                    "Only Fourier Test failed", "Only Entropy Test failed", "Only Runs Test failed"]

    #FOR RANDOM:
    aggregate_labels = ["No Tests failed", "Only Template Test failed", "Only Entropy Test failed",
                        "Only Fourier Test failed", "Only Monobit Test failed", "Only Longest Run Test failed",
                        "Only Frequency Test failed", "Only Runs Test failed"]
    RANDOMcounter_array = numpy.array([RANDOMmonoBitcounter, RANDOMduplicateCounter, RANDOMfrequencyCounter,
                                       RANDOMrunsCounter, RANDOMlongestRunCounter, RANDOMfourierCounter,
                                       RANDOMtemplateCounter, RANDOMentropyCounter])
    SESSIONIDcounter_array = numpy.array([SESSIONIDmonoBitcounter, SESSIONIDduplicateCounter, SESSIONIDfrequencyCounter,
                                       SESSIONIDrunsCounter, SESSIONIDlongestRunCounter, SESSIONIDfourierCounter,
                                       SESSIONIDtemplateCounter, SESSIONIDentropyCounter])
    IVcounter_array = numpy.array([IVmonoBitcounter, IVduplicateCounter, IVfrequencyCounter,
                                       IVrunsCounter, IVlongestRunCounter, IVfourierCounter,
                                       IVtemplateCounter, IVentropyCounter])
    COMPLETEcounter_array = numpy.array([COMPLETEmonoBitcounter, COMPLETEfrequencyCounter,
                                       COMPLETErunsCounter, COMPLETElongestRunCounter, COMPLETEfourierCounter,
                                       COMPLETEtemplateCounter, COMPLETEentropyCounter])

    unique, counts = numpy.unique(host_results, axis=0, return_counts=True)
    #graph_results = {tuple(i) : j for i, j in zip(unique, counts)}
    #graph_results = {k: v for k, v in sorted(graph_results.items(), key=lambda item: item[1], reverse=True)}

    #graph_results_clipped = dict(itertools.islice(graph_results.items(), 8))

    #print(graph_results)

    width = 0.30

    """
    
    fig, ax = plt.subplots()
    
    
    y_pos = numpy.arange(len(RANDOMcounter_array))
    
    rects1 = ax.bar(y_pos - 0.6666*width, RANDOMcounter_array, width, color='r', align='center')
    rects2 = ax.bar(y_pos + width/3, IVcounter_array, width, color='y', align='center')
    rects3 = ax.bar(y_pos + 1.3333*width, SESSIONIDcounter_array, width, color='g', align='center')
    
    ax.set_xticklabels(counter_labels)
    ax.set_xticks(y_pos + width / 3)
    
    ax.legend((rects1[0], rects2[0], rects3[0]), ('ServerHello Random', 'IV', 'Session ID'))
    
    ax.set_ylabel('Hosts failing Test')
    ax.set_title('Tests failed by randomness type')
    
    
    for rect in rects1:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 4, height),
                    xytext=(8, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    for rect in rects2:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 4, height),
                    xytext=(8, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    for rect in rects3:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 4, height),
                    xytext=(8, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    """

    y_pos = numpy.arange(len(COMPLETEcounter_array))

    plt.bar(y_pos, COMPLETEcounter_array, align='center', color='b')
    plt.xticks(y_pos, counter_labels_without_duplicate)
    plt.ylabel("Hosts failing Test")
    plt.title("Tests failed for Complete Sequences")

    for index, value in enumerate(COMPLETEcounter_array):
        plt.text(index, value, str(value), va='bottom', ha='center')

    # y_pos = numpy.arange(len(graph_results))
    # plt.hist(host_results)
    #x = numpy.arange(len(graph_results_clipped))
    #plt.bar(x, graph_results_clipped.values(), align='center', color='gold')
    #plt.xticks(x, graph_results_clipped.keys())
    # plt.title("Hosts with failed Complete Sequences")
    #plt.xlabel("Tests failed")
    #plt.ylabel("Hosts failing Test Combination")
    # plt.xticks(y_pos, counter_labels, rotation=45)
    #plt.xticks(x, aggregate_labels, rotation=45, ha='right')
    #plt.xticks(x, rotation=45, ha='right')

    #i = 0
    #for key in graph_results_clipped:
    #    plt.text(i, graph_results_clipped[key], str(graph_results_clipped[key]), va='bottom', ha='center')
    #    i = i+1


    print("Number of processed Hosts : "+str(len(list_of_hosts)))
    print("Hosts that failed MONOBIT with RANDOM : "+str(RANDOMmonoBitcounter))
    print("Hosts that failed DUPLICATE_TEST with RANDOM: "+str(RANDOMduplicateCounter))
    print("Hosts that failed FREQUENCY_TEST with RANDOM: "+str(RANDOMfrequencyCounter))
    print("Hosts that failed RUNS_TEST with RANDOM: "+str(RANDOMrunsCounter))
    print("Hosts that failed LONGEST_RUN_TEST with RANDOM: "+str(RANDOMlongestRunCounter))
    print("Hosts that failed FOURIER_TEST with RANDOM: "+str(RANDOMfourierCounter))
    print("Hosts that failed TEMPLATE_TEST with RANDOM: "+str(RANDOMtemplateCounter))
    print("Hosts that failed ENTROPY_TEST with RANDOM: "+str(RANDOMentropyCounter))

    plt.show()

else:
    list_of_hosts = set()

    RANDOMdieharder_0 = 0
    RANDOMdieharder_1 = 0
    RANDOMdieharder_2 = 0
    RANDOMdieharder_3 = 0
    RANDOMdieharder_13 = 0
    RANDOMdieharder_14 = 0
    RANDOMdieharder_15 = 0
    RANDOMdieharder_16 = 0
    RANDOMdieharder_17 = 0
    RANDOMdieharder_100 = 0
    RANDOMdieharder_101 = 0
    RANDOMdieharder_102 = 0
    RANDOMdieharder_200 = 0
    RANDOMdieharder_201 = 0
    RANDOMdieharder_202 = 0
    RANDOMdieharder_203 = 0
    RANDOMdieharder_204 = 0
    RANDOMdieharder_205 = 0
    RANDOMdieharder_206 = 0
    RANDOMdieharder_207 = 0
    RANDOMdieharder_208 = 0

    SESSIONIDdieharder_0 = 0
    SESSIONIDdieharder_1 = 0
    SESSIONIDdieharder_2 = 0
    SESSIONIDdieharder_3 = 0
    SESSIONIDdieharder_13 = 0
    SESSIONIDdieharder_14 = 0
    SESSIONIDdieharder_15 = 0
    SESSIONIDdieharder_16 = 0
    SESSIONIDdieharder_17 = 0
    SESSIONIDdieharder_100 = 0
    SESSIONIDdieharder_101 = 0
    SESSIONIDdieharder_102 = 0
    SESSIONIDdieharder_200 = 0
    SESSIONIDdieharder_201 = 0
    SESSIONIDdieharder_202 = 0
    SESSIONIDdieharder_203 = 0
    SESSIONIDdieharder_204 = 0
    SESSIONIDdieharder_205 = 0
    SESSIONIDdieharder_206 = 0
    SESSIONIDdieharder_207 = 0
    SESSIONIDdieharder_208 = 0

    IVdieharder_0 = 0
    IVdieharder_1 = 0
    IVdieharder_2 = 0
    IVdieharder_3 = 0
    IVdieharder_13 = 0
    IVdieharder_14 = 0
    IVdieharder_15 = 0
    IVdieharder_16 = 0
    IVdieharder_17 = 0
    IVdieharder_100 = 0
    IVdieharder_101 = 0
    IVdieharder_102 = 0
    IVdieharder_200 = 0
    IVdieharder_201 = 0
    IVdieharder_202 = 0
    IVdieharder_203 = 0
    IVdieharder_204 = 0
    IVdieharder_205 = 0
    IVdieharder_206 = 0
    IVdieharder_207 = 0
    IVdieharder_208 = 0

    COMPLETEdieharder_0 = 0
    COMPLETEdieharder_1 = 0
    COMPLETEdieharder_2 = 0
    COMPLETEdieharder_3 = 0
    COMPLETEdieharder_13 = 0
    COMPLETEdieharder_14 = 0
    COMPLETEdieharder_15 = 0
    COMPLETEdieharder_16 = 0
    COMPLETEdieharder_17 = 0
    COMPLETEdieharder_100 = 0
    COMPLETEdieharder_101 = 0
    COMPLETEdieharder_102 = 0
    COMPLETEdieharder_200 = 0
    COMPLETEdieharder_201 = 0
    COMPLETEdieharder_202 = 0
    COMPLETEdieharder_203 = 0
    COMPLETEdieharder_204 = 0
    COMPLETEdieharder_205 = 0
    COMPLETEdieharder_206 = 0
    COMPLETEdieharder_207 = 0
    COMPLETEdieharder_208 = 0

    hostArray = []

    print("Processing Data ...")

    for index, row in frame3.iterrows():
        hostName = row['host']
        if hostName not in list_of_hosts:
            currentHost = numpy.empty(21)

            result = row['dieharder_0']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_0 = RANDOMdieharder_0 + 1
                currentHost[0] = 1
            else:
                currentHost[0] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_0 = SESSIONIDdieharder_0 + 1

            if 'IV' in result_map:
                IVdieharder_0 = IVdieharder_0 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_0 = COMPLETEdieharder_0 + 1


            result = row['dieharder_1']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_1 = RANDOMdieharder_1 + 1
                currentHost[1] = 1
            else:
                currentHost[1] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_1 = SESSIONIDdieharder_1 + 1

            if 'IV' in result_map:
                IVdieharder_1 = IVdieharder_1 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_1 = COMPLETEdieharder_1 + 1


            result = row['dieharder_2']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_2 = RANDOMdieharder_2 + 1
                currentHost[2] = 1
            else:
                currentHost[2] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_2 = SESSIONIDdieharder_2 + 1

            if 'IV' in result_map:
                IVdieharder_2 = IVdieharder_2 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_2 = COMPLETEdieharder_2 + 1


            result = row['dieharder_3']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_3 = RANDOMdieharder_3 + 1
                currentHost[3] = 1
            else:
                currentHost[3] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_3 = SESSIONIDdieharder_3 + 1

            if 'IV' in result_map:
                IVdieharder_3 = IVdieharder_3 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_3 = COMPLETEdieharder_3 + 1


            result = row['dieharder_13']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_13 = RANDOMdieharder_13 + 1
                currentHost[4] = 1
            else:
                currentHost[4] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_13 = SESSIONIDdieharder_13 + 1

            if 'IV' in result_map:
                IVdieharder_13 = IVdieharder_13 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_13 = COMPLETEdieharder_13 + 1


            result = row['dieharder_14']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_14 = RANDOMdieharder_14 + 1
                currentHost[5] = 1
            else:
                currentHost[5] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_14 = SESSIONIDdieharder_14 + 1

            if 'IV' in result_map:
                IVdieharder_14 = IVdieharder_14 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_14 = COMPLETEdieharder_14 + 1


            result = row['dieharder_15']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_15 = RANDOMdieharder_15 + 1
                currentHost[6] = 1
            else:
                currentHost[6] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_15 = SESSIONIDdieharder_15 + 1

            if 'IV' in result_map:
                IVdieharder_15 = IVdieharder_15 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_15 = COMPLETEdieharder_15 + 1


            result = row['dieharder_16']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_16 = RANDOMdieharder_16 + 1
                currentHost[7] = 1
            else:
                currentHost[7] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_16 = SESSIONIDdieharder_16 + 1

            if 'IV' in result_map:
                IVdieharder_16 = IVdieharder_16 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_16 = COMPLETEdieharder_16 + 1


            result = row['dieharder_17']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_17 = RANDOMdieharder_17 + 1
                currentHost[8] = 1
            else:
                currentHost[8] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_17 = SESSIONIDdieharder_17 + 1

            if 'IV' in result_map:
                IVdieharder_17 = IVdieharder_17 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_17 = COMPLETEdieharder_17 + 1


            result = row['dieharder_100']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_100 = RANDOMdieharder_100 + 1
                currentHost[9] = 1
            else:
                currentHost[9] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_100 = SESSIONIDdieharder_100 + 1

            if 'IV' in result_map:
                IVdieharder_100 = IVdieharder_100 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_100 = COMPLETEdieharder_100 + 1


            result = row['dieharder_101']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_101 = RANDOMdieharder_101 + 1
                currentHost[10] = 1
            else:
                currentHost[10] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_101 = SESSIONIDdieharder_101 + 1

            if 'IV' in result_map:
                IVdieharder_101 = IVdieharder_101 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_101 = COMPLETEdieharder_101 + 1


            result = row['dieharder_102']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_102 = RANDOMdieharder_102 + 1
                currentHost[11] = 1
            else:
                currentHost[11] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_102 = SESSIONIDdieharder_102 + 1

            if 'IV' in result_map:
                IVdieharder_102 = IVdieharder_102 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_102 = COMPLETEdieharder_102 + 1


            result = row['dieharder_200']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_200 = RANDOMdieharder_200 + 1
                currentHost[12] = 1
            else:
                currentHost[12] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_200 = SESSIONIDdieharder_200 + 1

            if 'IV' in result_map:
                IVdieharder_200 = IVdieharder_200 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_200 = COMPLETEdieharder_200 + 1


            result = row['dieharder_201']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_201 = RANDOMdieharder_201 + 1
                currentHost[13] = 1
            else:
                currentHost[13] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_201 = SESSIONIDdieharder_201 + 1

            if 'IV' in result_map:
                IVdieharder_201 = IVdieharder_201 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_201 = COMPLETEdieharder_201 + 1


            result = row['dieharder_202']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_202 = RANDOMdieharder_202 + 1
                currentHost[14] = 1
            else:
                currentHost[14] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_202 = SESSIONIDdieharder_202 + 1

            if 'IV' in result_map:
                IVdieharder_202 = IVdieharder_202 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_202 = COMPLETEdieharder_202 + 1


            result = row['dieharder_203']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_203 = RANDOMdieharder_203 + 1
                currentHost[15] = 1
            else:
                currentHost[15] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_203 = SESSIONIDdieharder_203 + 1

            if 'IV' in result_map:
                IVdieharder_203 = IVdieharder_203 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_203 = COMPLETEdieharder_203 + 1


            result = row['dieharder_204']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_204 = RANDOMdieharder_204 + 1
                currentHost[16] = 1
            else:
                currentHost[16] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_204 = SESSIONIDdieharder_204 + 1

            if 'IV' in result_map:
                IVdieharder_204 = IVdieharder_204 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_204 = COMPLETEdieharder_204 + 1


            result = row['dieharder_205']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_205 = RANDOMdieharder_205 + 1
                currentHost[17] = 1
            else:
                currentHost[17] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_205 = SESSIONIDdieharder_205 + 1

            if 'IV' in result_map:
                IVdieharder_205 = IVdieharder_205 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_205 = COMPLETEdieharder_205 + 1


            result = row['dieharder_206']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_206 = RANDOMdieharder_206 + 1
                currentHost[18] = 1
            else:
                currentHost[18] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_206 = SESSIONIDdieharder_206 + 1

            if 'IV' in result_map:
                IVdieharder_206 = IVdieharder_206 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_206 = COMPLETEdieharder_206 + 1


            result = row['dieharder_207']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_207 = RANDOMdieharder_207 + 1
                currentHost[19] = 1
            else:
                currentHost[19] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_207 = SESSIONIDdieharder_207 + 1

            if 'IV' in result_map:
                IVdieharder_207 = IVdieharder_207 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_207 = COMPLETEdieharder_207 + 1

            result = row['dieharder_208']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_208 = RANDOMdieharder_208 + 1
                currentHost[20] = 1
            else:
                currentHost[20] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_208 = SESSIONIDdieharder_208 + 1

            if 'IV' in result_map:
                IVdieharder_208 = IVdieharder_208 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_208 = COMPLETEdieharder_208 + 1

            list_of_hosts.add(hostName)
            hostArray.append(currentHost)

    for index, row in frame4.iterrows():
        hostName = row['host']
        if hostName not in list_of_hosts:
            currentHost = numpy.empty(21)

            result = row['dieharder_0']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_0 = RANDOMdieharder_0 + 1
                currentHost[0] = 1
            else:
                currentHost[0] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_0 = SESSIONIDdieharder_0 + 1

            if 'IV' in result_map:
                IVdieharder_0 = IVdieharder_0 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_0 = COMPLETEdieharder_0 + 1


            result = row['dieharder_1']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_1 = RANDOMdieharder_1 + 1
                currentHost[1] = 1
            else:
                currentHost[1] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_1 = SESSIONIDdieharder_1 + 1

            if 'IV' in result_map:
                IVdieharder_1 = IVdieharder_1 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_1 = COMPLETEdieharder_1 + 1


            result = row['dieharder_2']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_2 = RANDOMdieharder_2 + 1
                currentHost[2] = 1
            else:
                currentHost[2] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_2 = SESSIONIDdieharder_2 + 1

            if 'IV' in result_map:
                IVdieharder_2 = IVdieharder_2 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_2 = COMPLETEdieharder_2 + 1


            result = row['dieharder_3']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_3 = RANDOMdieharder_3 + 1
                currentHost[3] = 1
            else:
                currentHost[3] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_3 = SESSIONIDdieharder_3 + 1

            if 'IV' in result_map:
                IVdieharder_3 = IVdieharder_3 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_3 = COMPLETEdieharder_3 + 1


            result = row['dieharder_13']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_13 = RANDOMdieharder_13 + 1
                currentHost[4] = 1
            else:
                currentHost[4] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_13 = SESSIONIDdieharder_13 + 1

            if 'IV' in result_map:
                IVdieharder_13 = IVdieharder_13 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_13 = COMPLETEdieharder_13 + 1


            result = row['dieharder_14']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_14 = RANDOMdieharder_14 + 1
                currentHost[5] = 1
            else:
                currentHost[5] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_14 = SESSIONIDdieharder_14 + 1

            if 'IV' in result_map:
                IVdieharder_14 = IVdieharder_14 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_14 = COMPLETEdieharder_14 + 1


            result = row['dieharder_15']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_15 = RANDOMdieharder_15 + 1
                currentHost[6] = 1
            else:
                currentHost[6] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_15 = SESSIONIDdieharder_15 + 1

            if 'IV' in result_map:
                IVdieharder_15 = IVdieharder_15 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_15 = COMPLETEdieharder_15 + 1


            result = row['dieharder_16']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_16 = RANDOMdieharder_16 + 1
                currentHost[7] = 1
            else:
                currentHost[7] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_16 = SESSIONIDdieharder_16 + 1

            if 'IV' in result_map:
                IVdieharder_16 = IVdieharder_16 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_16 = COMPLETEdieharder_16 + 1


            result = row['dieharder_17']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_17 = RANDOMdieharder_17 + 1
                currentHost[8] = 1
            else:
                currentHost[8] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_17 = SESSIONIDdieharder_17 + 1

            if 'IV' in result_map:
                IVdieharder_17 = IVdieharder_17 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_17 = COMPLETEdieharder_17 + 1


            result = row['dieharder_100']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_100 = RANDOMdieharder_100 + 1
                currentHost[9] = 1
            else:
                currentHost[9] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_100 = SESSIONIDdieharder_100 + 1

            if 'IV' in result_map:
                IVdieharder_100 = IVdieharder_100 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_100 = COMPLETEdieharder_100 + 1


            result = row['dieharder_101']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_101 = RANDOMdieharder_101 + 1
                currentHost[10] = 1
            else:
                currentHost[10] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_101 = SESSIONIDdieharder_101 + 1

            if 'IV' in result_map:
                IVdieharder_101 = IVdieharder_101 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_101 = COMPLETEdieharder_101 + 1


            result = row['dieharder_102']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_102 = RANDOMdieharder_102 + 1
                currentHost[11] = 1
            else:
                currentHost[11] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_102 = SESSIONIDdieharder_102 + 1

            if 'IV' in result_map:
                IVdieharder_102 = IVdieharder_102 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_102 = COMPLETEdieharder_102 + 1


            result = row['dieharder_200']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_200 = RANDOMdieharder_200 + 1
                currentHost[12] = 1
            else:
                currentHost[12] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_200 = SESSIONIDdieharder_200 + 1

            if 'IV' in result_map:
                IVdieharder_200 = IVdieharder_200 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_200 = COMPLETEdieharder_200 + 1


            result = row['dieharder_201']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_201 = RANDOMdieharder_201 + 1
                currentHost[13] = 1
            else:
                currentHost[13] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_201 = SESSIONIDdieharder_201 + 1

            if 'IV' in result_map:
                IVdieharder_201 = IVdieharder_201 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_201 = COMPLETEdieharder_201 + 1


            result = row['dieharder_202']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_202 = RANDOMdieharder_202 + 1
                currentHost[14] = 1
            else:
                currentHost[14] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_202 = SESSIONIDdieharder_202 + 1

            if 'IV' in result_map:
                IVdieharder_202 = IVdieharder_202 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_202 = COMPLETEdieharder_202 + 1


            result = row['dieharder_203']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_203 = RANDOMdieharder_203 + 1
                currentHost[15] = 1
            else:
                currentHost[15] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_203 = SESSIONIDdieharder_203 + 1

            if 'IV' in result_map:
                IVdieharder_203 = IVdieharder_203 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_203 = COMPLETEdieharder_203 + 1


            result = row['dieharder_204']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_204 = RANDOMdieharder_204 + 1
                currentHost[16] = 1
            else:
                currentHost[16] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_204 = SESSIONIDdieharder_204 + 1

            if 'IV' in result_map:
                IVdieharder_204 = IVdieharder_204 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_204 = COMPLETEdieharder_204 + 1


            result = row['dieharder_205']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_205 = RANDOMdieharder_205 + 1
                currentHost[17] = 1
            else:
                currentHost[17] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_205 = SESSIONIDdieharder_205 + 1

            if 'IV' in result_map:
                IVdieharder_205 = IVdieharder_205 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_205 = COMPLETEdieharder_205 + 1


            result = row['dieharder_206']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_206 = RANDOMdieharder_206 + 1
                currentHost[18] = 1
            else:
                currentHost[18] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_206 = SESSIONIDdieharder_206 + 1

            if 'IV' in result_map:
                IVdieharder_206 = IVdieharder_206 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_206 = COMPLETEdieharder_206 + 1


            result = row['dieharder_207']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_207 = RANDOMdieharder_207 + 1
                currentHost[19] = 1
            else:
                currentHost[19] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_207 = SESSIONIDdieharder_207 + 1

            if 'IV' in result_map:
                IVdieharder_207 = IVdieharder_207 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_207 = COMPLETEdieharder_207 + 1

            result = row['dieharder_208']
            result_map = process_string(result)
            if 'RANDOM' in result_map:
                RANDOMdieharder_208 = RANDOMdieharder_208 + 1
                currentHost[20] = 1
            else:
                currentHost[20] = 0

            if 'SESSION_ID' in result_map:
                SESSIONIDdieharder_208 = SESSIONIDdieharder_208 + 1

            if 'IV' in result_map:
                IVdieharder_208 = IVdieharder_208 + 1

            if 'COMPLETE_SEQUENCE' in result_map:
                COMPLETEdieharder_208 = COMPLETEdieharder_208 + 1

            list_of_hosts.add(hostName)
            hostArray.append(currentHost)

    print("Data processed!")

    host_results = numpy.stack(hostArray, 0)

    dieharder_labels_one = ["Birthdays Test", "Overlapping 5-Permutation Test", "32x32 Binary Rank Test",
                            "6x8 Binary Rank Test", "Squeeze Test", "Sums Test", "Runs Test (DIEHARDER)", "Craps Test"]
    dieharder_labels_two = ["GCD Test", "Monobit Test (DIEHARDER)", "Runs Test (NIST)", "Serial Test (DIEHARDER)",
                            "Bit Distribution Test", "Minimum Distance Test", "Permutation Test", "Lagged Sums Test"]
    dieharder_labels_three = ["Kolmogorov-Smirnov Test", "Byte Distribution Test", "DCT (Frequency Analysis) Test",
                              "Fill Tree Test", "Fill Tree 2 Test"]

    dieharder_all_labels = ["Birthdays Test", "Overlapping 5-Permutation Test", "32x32 Binary Rank Test",
                            "6x8 Binary Rank Test", "Squeeze Test", "Sums Test", "Runs Test (DIEHARDER)", "Craps Test",
                            "GCD Test", "Monobit Test (DIEHARDER)", "Serial Test (DIEHARDER)", "Bit Distribution Test",
                            "Minimum Distance Test", "Permutation Test", "Lagged Sums Test", "Kolmogorov-Smirnov Test",
                            "Byte Distribution Test", "DCT (Frequency Analysis) Test", "Fill Tree Test",
                            "Fill Tree 2 Test"]

    RANDOMcounter_array = numpy.array([RANDOMdieharder_0, RANDOMdieharder_1, RANDOMdieharder_2,
                                       RANDOMdieharder_3, RANDOMdieharder_13, RANDOMdieharder_14,
                                       RANDOMdieharder_15, RANDOMdieharder_16, RANDOMdieharder_17,
                                       RANDOMdieharder_100, RANDOMdieharder_101, RANDOMdieharder_102,
                                       RANDOMdieharder_200, RANDOMdieharder_201, RANDOMdieharder_202,
                                       RANDOMdieharder_203, RANDOMdieharder_204, RANDOMdieharder_205,
                                       RANDOMdieharder_206, RANDOMdieharder_207, RANDOMdieharder_208])

    SESSIONIDcounter_array = numpy.array([SESSIONIDdieharder_0, SESSIONIDdieharder_1, SESSIONIDdieharder_2,
                                          SESSIONIDdieharder_3, SESSIONIDdieharder_13, SESSIONIDdieharder_14,
                                          SESSIONIDdieharder_15, SESSIONIDdieharder_16, SESSIONIDdieharder_17,
                                          SESSIONIDdieharder_100, SESSIONIDdieharder_101, SESSIONIDdieharder_102,
                                          SESSIONIDdieharder_200, SESSIONIDdieharder_201, SESSIONIDdieharder_202,
                                          SESSIONIDdieharder_203, SESSIONIDdieharder_204, SESSIONIDdieharder_205,
                                          SESSIONIDdieharder_206, SESSIONIDdieharder_207, SESSIONIDdieharder_208])

    IVcounter_array = numpy.array([IVdieharder_0, IVdieharder_1, IVdieharder_2,
                                   IVdieharder_3, IVdieharder_13, IVdieharder_14,
                                   IVdieharder_15, IVdieharder_16, IVdieharder_17,
                                   IVdieharder_100, IVdieharder_101, IVdieharder_102,
                                   IVdieharder_200, IVdieharder_201, IVdieharder_202,
                                   IVdieharder_203, IVdieharder_204, IVdieharder_205,
                                   IVdieharder_206, IVdieharder_207, IVdieharder_208])

    COMPLETEcounter_array = numpy.array([COMPLETEdieharder_0, COMPLETEdieharder_1, COMPLETEdieharder_2,
                                         COMPLETEdieharder_3, COMPLETEdieharder_13, COMPLETEdieharder_14,
                                         COMPLETEdieharder_15, COMPLETEdieharder_16, COMPLETEdieharder_17,
                                         COMPLETEdieharder_100, COMPLETEdieharder_101, COMPLETEdieharder_102,
                                         COMPLETEdieharder_200, COMPLETEdieharder_201, COMPLETEdieharder_202,
                                         COMPLETEdieharder_203, COMPLETEdieharder_204, COMPLETEdieharder_205,
                                         COMPLETEdieharder_206, COMPLETEdieharder_207, COMPLETEdieharder_208])

    width = 0.20

    fig, ax = plt.subplots()

    y_pos = numpy.arange(len(RANDOMcounter_array[16:]))

    # Only First 8 elements
    rects1 = ax.bar(y_pos, RANDOMcounter_array[16:], width, color='r')
    rects2 = ax.bar(y_pos + 1*width, IVcounter_array[16:], width, color='y')
    rects3 = ax.bar(y_pos + 2*width, SESSIONIDcounter_array[16:], width, color='g')
    rects4 = ax.bar(y_pos + 3*width, COMPLETEcounter_array[16:], width, color='b')


    ax.set_xticklabels(dieharder_labels_three, rotation=45, horizontalalignment="right")
    ax.set_xticks(y_pos + 1.5*width)

    ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('ServerHello Random', 'IV', 'Session ID', "Complete"))

    ax.set_ylabel('Hosts failing Test')
    ax.set_title('Tests failed by randomness type')


    for rect in rects1:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 4, height),
                    xytext=(6, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    for rect in rects2:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 4, height),
                    xytext=(6, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    for rect in rects3:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 4, height),
                    xytext=(6, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    for rect in rects4:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 4, height),
                    xytext=(6, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.show()