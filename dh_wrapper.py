import os
import subprocess


class DieHarderWrapper:
    def __init__(self, filename):
        self.test_results = self.populate_test_results()
        self.test_parameters = self.populate_test_parameters()
        if isinstance(filename, str) and len(filename) > 0:
            self.filename = filename
        else:
            raise Exception("Filepath should be a String with at least one character.")

    @staticmethod
    def populate_test_results():
        test_results = dict()

        for i in range(0, 18):
            if i not in range(4, 13):
                test_results[i] = ["UNTESTED"]

        for i in range(100, 103):
            test_results[i] = ["UNTESTED"]

        for i in range(200, 209):
            test_results[i] = ["UNTESTED"]

        return test_results

    @staticmethod
    def populate_test_parameters():
        test_parameters = dict()

        # Structure: test_parameters[x] = [a,b,c]
        # where
        # x = diehard test number
        # a = number of t-samples utilizied in test
        # b = number of p-values calculated in test
        # c = additional parameters (like n-tuples etc.)
        # NOTE: These parameters are entirely based on local tests and are not based on any scientific results.

        test_parameters[0] = [20, 1, ""]
        test_parameters[1] = [35, 100, ""]
        test_parameters[2] = [15, 10, ""]
        test_parameters[3] = [25, 25, ""]
        test_parameters[13] = [64, 5, ""]
        test_parameters[14] = [20, 100, ""]
        test_parameters[15] = [5000, 1, ""]
        test_parameters[16] = [21, 30, ""]
        test_parameters[17] = [6000, 1, ""]
        test_parameters[100] = [40, 100, "-n 1"]
        test_parameters[101] = [40, 100, "-n 2"]
        test_parameters[102] = [40, 100, ""]
        test_parameters[200] = [175, 10, "-n 2"]
        test_parameters[201] = [600, 10, "-n 2"]
        test_parameters[202] = [600, 1, ""]
        test_parameters[203] = [40, 10, "-n 2"]
        test_parameters[204] = [590, 10, ""]
        test_parameters[205] = [1280, 1, ""]
        test_parameters[206] = [18, 1, ""]
        test_parameters[207] = [270, 1, ""]
        test_parameters[208] = [306, 1, ""]

        return test_parameters

    def execute_all_tests(self):
        for i in range(0, 18):
            if i not in range(4, 13):
                self.execute_test(self, i)

        for i in range(100, 103):
            self.execute_test(self, i)

        for i in range(200, 209):
            self.execute_test(self, i)

    def execute_test(self, test_number):

        if test_number is None:
            raise Exception("No test_number specified. Aborting.")

        if test_number not in self.test_parameters.keys():
            print("test number not known / not supported.")
            return

        parameters = self.test_parameters.get(test_number)
        t_numbers = parameters[0]
        p_numbers = parameters[1]
        additional_params = parameters[2]

        parameters = "-d "+str(test_number)+" -t "+str(t_numbers)+" -p "+str(p_numbers)+" "+additional_params
        # Note: -s 1 = always start at the start of the file when starting new tests
        # Note: -D 256 = only output if Tests are passed/failed or weak
        # Note: -g 202 = Use File-Input and formatted Files fit for Dieharder
        # NOTE: REQUIRES PYTHON 3.5 OR HIGHER!
        result = subprocess.run("dieharder -D 256 -s 1 -g 202 -f "+self.filename+" "+parameters, shell=True,
                                stdout=subprocess.PIPE)

        output = result.stdout.decode('utf-8')

        self.test_results[test_number] = []

        for i in range(0, output.count("PASSED")):
            self.test_results[test_number].append("PASSED")

        for i in range(0, output.count("WEAK")):
            self.test_results[test_number].append("WEAK")

        for i in range(0, output.count("FAILED")):
            self.test_results[test_number].append("FAILED")

    def return_results(self):
        return self.test_results
