from multiprocessing import Process
import subprocess
import itertools
import base64
import os
import textwrap


def __init__(self, document):
    self.document = document
    self.hello_random = None
    self.session_id_random = None
    self.iv_random = None
    self.complete_sequence = None
    self.host_name = None
    extract_randoms()
    test_host()


def extract_randoms(self):
    db_rand = self.document['result']['report']['extractedRandomList']
    db_sess_id = self.document['result']['report']['extractedSessionIDList']
    db_iv = self.document['result']['report']['extractedIVList']
    self.host_name = self.document['scanTarget']['hostname']

    # extracting the random data from the document
    if db_rand is not None:
        # self.hello_random = []
        integer_file_random = open('/tmp/'+self.host_name+'_hello.RAND', "w")
        # TODO: Write Header for File for Dieharder
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
        # TODO: Write Header for Dieharder
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
        # TODO: Write Header for Dieharder
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
    #TODO : Write Header for Dieharder
    for package in splitter:
        converted_int = int(package, 16)
        integer_file_iv.write(str(converted_int)+'\n')
    complete_file.close()


def test_host(self):
    # Diehard Parameters: -d $TEST_NUMBER -t $T_SAMPLES -g 202 -f $FILE_NAME -s 1
    # Some Tests have to adapt n tuples via -n for tests on short bit strings i.e.
    # Diehard Parameters: -d $TEST_NUMBER -t $T_SAMPLES -g 202 -f $FILE_NAME -n $TUPLE_NUMBERS -s 1
    # Parameters:
    # -g 202 --> read file instead of sampling real generator
    # -s 1 --> reseed/rewind at the beginning of each test, instead of only at the start of the test-battery.
    # NOTE: Some tests have additional parameters available, which can be set via -x -y -z
    command = "dieharder"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    # do something after execution
