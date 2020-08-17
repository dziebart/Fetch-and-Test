import os
import textwrap
from dh_wrapper import DieHarderWrapper
from stat_result import StatisticalResults


class FetchSlave:

    def __init__(self, document):
        """
        Slave class, which is invoked by the master class and takes a document, which is a representation of a host,
        defined by previous test results and lists of extracted randomness data.
        @param document: the mongoDB document representing a scanned host.
        """
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
        successful = self.extract_randoms()
        if successful:
            self.test_randoms()
        self.clean_up()

    def extract_previous_results(self):
        """
        Extracts previous test data available in the MongoDB and prepares it for combination with the new
        test results provided by dieharder.
        """
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
        """
        Extracts the randomness data from the list of arrays provided by the MongoDB entry. The randomness data is then
        prepared into distinct lists and written into temporary files for analysis with dieharder.
        """
        self.hello_random = self.document['result']['report']['extractedRandomList']
        self.session_id_random = self.document['result']['report']['extractedSessionIDList']
        self.iv_random = self.document['result']['report']['extractedIVList']

        if self.hello_random is None and self.session_id_random is None and self.iv_random is None:
            # Nothing to extract.
            return False

        # extracting the random data from the document
        if self.hello_random is not None:
            # self.hello_random = []
            integer_file_random = open(self.hello_random_filename, "w")
            number_of_integers = len(self.hello_random) * (len(self.hello_random[0].get('array'))/8)
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
            number_of_integers = len(self.session_id_random) * (len(self.session_id_random[0].get('array'))/8)
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
            number_of_integers = len(self.iv_random) * (len(self.iv_random[0].get('array'))/8)
            self.write_header(integer_file_iv, number_of_integers)
            for rand in self.iv_random:
                # self.iv_random.append(rand.get('array'))
                splitter = textwrap.wrap(rand.get('array'), 8)
                for package in splitter:
                    converted_int = int(package, 16)
                    integer_file_iv.write(str(converted_int) + "\n")
            integer_file_iv.close()

        self.complete_sequence = ""

        hello_random_length = 0
        session_id_length = 0

        if self.hello_random is not None:
            hello_random_length = len(self.hello_random)

        if self.session_id_random is not None:
            session_id_length = len(self.session_id_random)

        for i in range(0, max(hello_random_length, session_id_length)):
            if not self.hello_random[i] is None:
                self.complete_sequence = self.complete_sequence + self.hello_random[i].get('array')
            if not self.session_id_random[i] is None:
                self.complete_sequence = self.complete_sequence + self.session_id_random[i].get('array')

        if self.iv_random is not None:
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

        return True

    @staticmethod
    def write_header(file, number_of_ints):
        """
        Writes the header for the file required by dieharder.
        @param file: file object, which is used to write the header
        @param number_of_ints: how many integers are listed in the file itself.
        """
        file.write("#==================================================================\n")
        file.write("# generator online  seed = 0000000\n")
        file.write("#==================================================================\n")
        file.write("type: d\n")
        file.write("count: " + str(int(number_of_ints)) + "\n")
        file.write("numbit: 32\n")

    def test_randoms(self):
        """
        Uses the dieharder wrapper to test the extracted randomness data and save the results to seperate lists. Creates
        a StatisticalResult object, which is the combination of the previous and new results.
        """
        if os.path.exists(self.hello_random_filename) and self.hello_random is not None and len(self.hello_random) > 0:
            dieharder = DieHarderWrapper(self.hello_random_filename)
            dieharder.execute_all_tests()
            hello_random_results = dieharder.get_results()
        else:
            raise Exception("File "+self.hello_random_filename+" not found.")

        if os.path.exists(self.session_random_filename) and self.session_id_random is not None \
                and len(self.session_id_random) > 0:
            dieharder = DieHarderWrapper(self.session_random_filename)
            dieharder.execute_all_tests()
            session_random_results = dieharder.get_results()
        else:
            raise Exception("File "+self.session_random_filename+" not found.")

        if os.path.exists(self.iv_random_filename) and self.iv_random is not None and len(self.iv_random) > 0:
            dieharder = DieHarderWrapper(self.iv_random_filename)
            dieharder.execute_all_tests()
            iv_random_results = dieharder.get_results()
        else:
            raise Exception("File "+self.iv_random_filename+" not found.")

        if os.path.exists(self.complete_random_filename) and self.complete_sequence is not None \
                and len(self.complete_sequence) > 0:
            dieharder = DieHarderWrapper(self.complete_random_filename)
            dieharder.execute_all_tests()
            complete_random_results = dieharder.get_results()
        else:
            raise Exception("File "+self.complete_random_filename+" not found.")

        self.stat_results = StatisticalResults(self.host_name, self.previous_results, self.template_percentage_map,
                                               hello_random_results, session_random_results,
                                               iv_random_results, complete_random_results,
                                               self.unixTime, self.prematureStop)

    def clean_up(self):
        """
        Removes the temporary files containing the formatted randomn data for dieharder testing.
        """
        if os.path.exists(self.hello_random_filename):
            os.remove(self.hello_random_filename)

        if os.path.exists(self.session_random_filename):
            os.remove(self.session_random_filename)

        if os.path.exists(self.iv_random_filename):
            os.remove(self.iv_random_filename)

        if os.path.exists(self.complete_random_filename):
            os.remove(self.complete_random_filename)

    def get_results(self):
        """
        Returns the StatisticalResults object containg all test data.
        @return: StatisticalResults object containg all test data.
        """
        return self.stat_results
