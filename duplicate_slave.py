import os
import textwrap
from dh_wrapper import DieHarderWrapper
from stat_result import StatisticalResults


class DuplicateSlave:

    def __init__(self, document, byte_size):
        """
        Slave class for detection of potential duplicates of complete sequences.
        @param document: the mongoDB document representing a scanned host.
        """
        self.document = document
        self.byte_size = byte_size
        self.hello_random = None
        self.session_id_random = None
        self.iv_random = None
        self.complete_sequence = None
        self.host_name = self.document['scanTarget']['hostname']
        self.duplicate_result = False
        successful = self.test_duplicate()

    def test_duplicate(self):
        """
        Extracts randomness data and checks for duplicates in complete sequence
        """
        self.hello_random = self.document['result']['report']['extractedRandomList']
        self.session_id_random = self.document['result']['report']['extractedSessionIDList']
        self.iv_random = self.document['result']['report']['extractedIVList']

        if (self.hello_random is None or len(self.hello_random) == 0) and \
                (self.session_id_random is None or len(self.session_id_random) == 0) and \
                (self.iv_random is None or len(self.iv_random) == 0):
            # Nothing to extract.
            return False

        self.complete_sequence = ""

        hello_random_length = 0
        session_id_length = 0

        if self.hello_random is not None:
            hello_random_length = len(self.hello_random)

        if self.session_id_random is not None:
            session_id_length = len(self.session_id_random)

        for i in range(0, max(hello_random_length, session_id_length)):
            if i < hello_random_length and self.hello_random[i] is not None:
                self.complete_sequence = self.complete_sequence + self.hello_random[i].get('array')
            if i < session_id_length and self.session_id_random[i] is not None:
                self.complete_sequence = self.complete_sequence + self.session_id_random[i].get('array')

        if self.iv_random is not None:
            for iv in self.iv_random:
                if iv is not None:
                    self.complete_sequence = self.complete_sequence + iv.get('array')

        list_of_bytes = set()

        complete_sequence_wrap = textwrap.wrap(self.complete_sequence, self.byte_size)

        for byte_pack in complete_sequence_wrap:
            if byte_pack in list_of_bytes:
                self.duplicate_result = True
            else:
                list_of_bytes.add(byte_pack)

        if(self.duplicate_result is True):
            print(self.host_name)

        return True

    def get_results(self):
        """
        Returns the result of the Duplicate Check.
        @return: True or False.
        """
        return self.duplicate_result
