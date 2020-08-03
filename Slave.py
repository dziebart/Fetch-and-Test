from multiprocessing import Process
import subprocess
import itertools
import base64

def __init__(self, document):
    self.document = document
    self.hello_random = None
    self.session_id_random = None
    self.iv_random = None
    self.complete_sequence = None
    extract_randoms()
    test_host()


def extract_randoms(self):
    db_rand = self.document['result']['report']['extractedRandomList']
    db_sess_id = self.document['result']['report']['extractedSessionIDList']
    db_iv = self.document['result']['report']['extractedIVList']

    # extracting the random data from the document
    if db_rand is not None:
        self.hello_random = []
        for rand in db_rand:
            self.hello_random.append(rand.get('array'))

    if db_sess_id is not None:
        self.session_id_random = []
        for rand in db_sess_id:
            self.session_id_random.append(rand.get('array'))

    if db_iv is not None:
        self.iv_random = []
        for rand in db_iv:
            self.iv_random.append(rand.get('array'))

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


def test_host(self):
    # Applied Tests are:
    # For ~20 KB
    # 1) Birthdays Test --> for t=1 is rewound 8 times
    # 2) 32x32 Rank test (? Maybe not enough samples) --> rewound 28750 times
    # 3) 6x8 Rank Test (see above) ---> rewound 14583 times
    # 4) Bistream Test (Overlapping version) --> rewound 7544 times
    # 5) Count the 1s ---> rewound 3416 times
    # 6) Count the 1s (byte) ---> rewound 28750 times
    # 7) Parking Lot Test (Not enough samples?) ---> rewound 2583 times
    # 8) Minimum Distance Test (Not enough samples?) --> rewound 2416 times
    # 9) Minimum Distance 3D Test ( Not enough samples?) --> rewound 2333 times
    # 10) Squeeze Test --> rewound 49031 times
    # 11) Runs test (Default samples of 100000 --> Not enough samples?) --> rewound 4166 times
    # 12) Craps Test --> rewound 30613 times
    # 13) Marsaglia and Tsang GCD Test --> etc.
    # 14) Maybe STS Serial Test, see how long it takes.
    # 15) RGB Bit Distribution Test
    # 16) Generalized Minimum Distance Test
    # 17) RGB Permutations Test
    # 18) RGB Lagged Sum Test
    # 19) Kolmogorov-Smirnov test
    # 20) DAB Tests - examine run time
    # --> NOTE: ALL TESTS FAILED WITH THIS AMOUNT OF RANDOM BYTES!
    # --> NOTE: Play around with the t-values appropriate for these numbers.
    # --> NOTE: For Exampel t=100 seems to be a good start for reasonable numbers for some tests
    # NOTE: LAGGED SUM TAKES A LONG TIME!
    # Files are rewound many times --> play around with the settings.
    # Save to file instead of stdinput to support rewind.
    command = "dieharder"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    # do something after execution
