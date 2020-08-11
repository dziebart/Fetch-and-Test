import os
import textwrap
from dh_wrapper import DieHarderWrapper
from stat_result import StatisticalResults


class FetchSlave:

    def __init__(self, document):
        self.document = document
        self.hello_random = None
        self.session_id_random = None
        self.iv_random = None
        self.complete_sequence = None
        self.host_name = self.document['scanTarget']['hostname']
        self.hello_random_filename = '/tmp/'+self.host_name+'_hello.RAND'
        self.session_random_filename = '/tmp/'+self.host_name+'_session.RAND'
        self.iv_random_filename = '/tmp/'+self.host_name+'_iv.RAND'
        self.complete_random_filename = '/tmp/'+self.host_name+'_complete.RAND'
        self.previous_results = None
        self.template_percentage_map = None
        self.unixTime = None
        self.prematureStop = None
        self.stat_results = None
        self.extract_previous_results()
        self.extract_randoms()
        self.test_randoms()
        self.clean_up()

    def extract_previous_results(self):
        self.previous_results = dict()

        self.previous_results["randomDuplicatesResult"] = self.document['result']['report']['randomDuplicatesResult']
        self.previous_results["monoBitResult"] = self.document['result']['report']['monoBitResult']
        self.previous_results["frequencyResult"] = self.document['result']['report']['frequencyResult']
        self.previous_results["runsResult"] = self.document['result']['report']['runsResult']
        self.previous_results["longestRunBlockResult"] = self.document['result']['report']['longestRunBlockResult']
        self.previous_results["fourierResult"] = self.document['result']['report']['fourierResult']
        self.previous_results["templateResult"] = self.document['result']['report']['templateResult']
        self.previous_results["entropyResult"] = self.document['result']['report']['entropyResult']

        self.template_percentage_map = self.document['result']['report']['templatePercentageMap']

        self.prematureStop = self.document['result']['report']['prematureStopResult']
        self.unixTime = self.document['result']['report']['unixtimeResult']

    def extract_randoms(self):
        self.hello_random = self.document['result']['report']['extractedRandomList']
        self.session_id_random = self.document['result']['report']['extractedSessionIDList']
        self.iv_random = self.document['result']['report']['extractedIVList']

        # extracting the random data from the document
        if self.hello_random is not None:
            # self.hello_random = []
            integer_file_random = open(self.hello_random_filename, "w")
            number_of_integers = len(self.hello_random)*8
            self.write_header(integer_file_random, number_of_integers)
            for rand in self.hello_random:
                # self.hello_random.append(rand.get('array'))
                splitter = textwrap.wrap(rand.get('array'), 8)
                for package in splitter:
                    converted_int = int(package, 16)
                    integer_file_random.write(str(converted_int) + "\n")
            integer_file_random.close()

        if self.session_id_random is not None:
            # self.session_id_random = []
            integer_file_session = open(self.session_random_filename, "w")
            number_of_integers = len(self.session_id_random) * 8
            self.write_header(integer_file_session, number_of_integers)
            for rand in self.session_id_random:
                # self.session_id_random.append(rand.get('array'))
                splitter = textwrap.wrap(rand.get('array'), 8)
                for package in splitter:
                    converted_int = int(package, 16)
                    integer_file_session.write(str(converted_int) + "\n")
            integer_file_session.close()

        if self.iv_random is not None:
            # self.iv_random = []
            integer_file_iv = open(self.iv_random_filename, "w")
            number_of_integers = len(self.iv_random) * 4
            self.write_header(integer_file_iv, number_of_integers)
            for rand in self.iv_random:
                # self.iv_random.append(rand.get('array'))
                splitter = textwrap.wrap(rand.get('array'), 8)
                for package in splitter:
                    converted_int = int(package, 16)
                    integer_file_iv.write(str(converted_int) + "\n")
            integer_file_iv.close()

        self.complete_sequence = ""

        for i in range(0, max(len(self.hello_random), len(self.session_id_random))):
            if not self.hello_random[i] is None:
                self.complete_sequence = self.complete_sequence + self.hello_random[i].get('array')
            if not self.session_id_random[i] is None:
                self.complete_sequence = self.complete_sequence + self.session_id_random[i].get('array')

        for iv in self.iv_random:
            if iv is not None:
                self.complete_sequence = self.complete_sequence + iv.get('array')

        # Write File in pack of 4 Bytes
        complete_file = open(self.complete_random_filename, "w")
        splitter = textwrap.wrap(self.complete_sequence, 8)
        self.write_header(complete_file, len(splitter))
        for package in splitter:
            converted_int = int(package, 16)
            complete_file.write(str(converted_int)+'\n')
        complete_file.close()

    @staticmethod
    def write_header(file, number_of_ints):
        file.write("#==================================================================\n")
        file.write("# generator online  seed = 0000000\n")
        file.write("#==================================================================\n")
        file.write("type: d\n")
        file.write("count: " + str(number_of_ints) + "\n")
        file.write("numbit: 32\n")

    def test_randoms(self):
        if os.path.exists(self.hello_random_filename):
            dieharder = DieHarderWrapper(self.hello_random_filename)
            dieharder.execute_all_tests()
            hello_random_results = dieharder.get_results()
        else:
            raise Exception("File "+self.hello_random_filename+" not found.")

        if os.path.exists(self.session_random_filename):
            dieharder = DieHarderWrapper(self.session_random_filename)
            dieharder.execute_all_tests()
            session_random_results = dieharder.get_results()
        else:
            raise Exception("File "+self.session_random_filename+" not found.")

        if os.path.exists(self.iv_random_filename):
            dieharder = DieHarderWrapper(self.iv_random_filename)
            dieharder.execute_all_tests()
            iv_random_results = dieharder.get_results()
        else:
            raise Exception("File "+self.iv_random_filename+" not found.")

        if os.path.exists(self.complete_random_filename):
            dieharder = DieHarderWrapper(self.complete_random_filename)
            dieharder.execute_all_tests()
            complete_random_results = dieharder.get_results()
        else:
            raise Exception("File "+self.complete_random_filename+" not found.")

        self.stat_results = StatisticalResults(self.previous_results, self.template_percentage_map,
                                               hello_random_results, session_random_results,
                                               iv_random_results, complete_random_results,
                                               self.unixTime, self.prematureStop)

    def clean_up(self):
        if os.path.exists(self.hello_random_filename):
            os.remove(self.hello_random_filename)

        if os.path.exists(self.session_random_filename):
            os.remove(self.session_random_filename)

        if os.path.exists(self.iv_random_filename):
            os.remove(self.iv_random_filename)

        if os.path.exists(self.complete_random_filename):
            os.remove(self.complete_random_filename)

    def get_results(self):
        return self.stat_results