from multiprocessing import Process
import subprocess
import itertools
import base64
import os
import textwrap
import dh_wrapper


class FetchSlave:

    def __init__(self, document):
        self.document = document
        self.hello_random = None
        self.session_id_random = None
        self.iv_random = None
        self.complete_sequence = None
        self.host_name = self.document['scanTarget']['hostname']
        self.previous_results = None
        self.template_percentage_map = None
        self.unixTime = None
        self.prematureStop = None
        self.new_results = None
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
        db_rand = self.document['result']['report']['extractedRandomList']
        db_sess_id = self.document['result']['report']['extractedSessionIDList']
        db_iv = self.document['result']['report']['extractedIVList']

        # extracting the random data from the document
        if db_rand is not None:
            # self.hello_random = []
            integer_file_random = open('/tmp/'+self.host_name+'_hello.RAND', "w")
            number_of_integers = len(db_rand)*8
            self.write_header(integer_file_random, number_of_integers)
            for rand in db_rand:
                # self.hello_random.append(rand.get('array'))
                splitter = textwrap.wrap(rand.get('array'), 8)
                for package in splitter:
                    converted_int = int(package, 16)
                    integer_file_random.write(str(converted_int) + "\n")
            integer_file_random.close()

        if db_sess_id is not None:
            # self.session_id_random = []
            integer_file_session = open('/tmp/'+self.host_name+'_session.RAND', "w")
            number_of_integers = len(db_sess_id) * 8
            self.write_header(integer_file_session, number_of_integers)
            for rand in db_sess_id:
                # self.session_id_random.append(rand.get('array'))
                splitter = textwrap.wrap(rand.get('array'), 8)
                for package in splitter:
                    converted_int = int(package, 16)
                    integer_file_session.write(str(converted_int) + "\n")
            integer_file_session.close()

        if db_iv is not None:
            # self.iv_random = []
            integer_file_iv = open('/tmp'+self.host_name+'_iv.RAND', "w")
            number_of_integers = len(db_iv) * 4
            self.write_header(integer_file_iv, number_of_integers)
            for rand in db_iv:
                # self.iv_random.append(rand.get('array'))
                splitter = textwrap.wrap(rand.get('array'), 8)
                for package in splitter:
                    converted_int = int(package, 16)
                    integer_file_iv.write(str(converted_int) + "\n")
            integer_file_iv.close()

        # constructing the complete sequence
        for rand, session_id in itertools.zip_longest(self.hello_random, self.session_id_random):
            append_string = ""
            if rand is not None:
                append_string = append_string + rand
            if session_id is not None:
                append_string = append_string + session_id

        for iv in self.iv_random:
            if iv is not None:
                append_string = append_string + iv

        self.complete_sequence = append_string

        # Write File in pack of 4 Bytes
        complete_file = open('/tmp/'+self.host_name+'_complete.RAND', "w")
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
        print("Do stuff")

    def clean_up(self):
        if os.path.exists('/tmp/'+self.host_name+'_hello.RAND'):
            os.remove('/tmp/'+self.host_name+'_hello.RAND')

        if os.path.exists('/tmp/'+self.host_name+'_session.RAND'):
            os.remove('/tmp/'+self.host_name+'_session.RAND')

        if os.path.exists('/tmp'+self.host_name+'_iv.RAND'):
            os.remove('/tmp'+self.host_name+'_iv.RAND')

        if os.path.exists('/tmp/'+self.host_name+'_complete.RAND'):
            os.remove('/tmp/'+self.host_name+'_complete.RAND')