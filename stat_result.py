import sqlalchemy


class StatisticalResults:

    def __init__(self, host_name, previous_results, template_percentage_map,
                 hello_random_results, session_random_results, iv_random_results,
                 complete_random_results, uses_unix_time, premature_stop):
        """
        Creates a wrapper object, which holds the previous results from the TLS-Scanner RNG-Probe and the new results
        from the Dieharder test-battery using dicts. In addition to that, this class also holds two boolean values
        related to the behaviour and scanning procedure of the scanned host. This class acts as a wrapper for all these
        values, so the "slave" can return all required results to the "master" in one method.
        @param host_name: Name of the scanned host
        @param previous_results: dict containing the test results from the TLS-Scanner RNG-Probe
        @param template_percentage_map: dict containing the template test results from the TLS-Scanner RNG-Probe
        @param hello_random_results: dict containing the results from the dieharder tests on the serverHello randoms
        @param session_random_results: dict containing the results from the dieharder tests on the sessionIDs
        @param iv_random_results: dict containing the results from the dieharder tests on the initialization vectors
        @param complete_random_results: dict containing the results from the dieharder tests on the complete sequence
        @param uses_unix_time: TRUE if the host uses unixTime (or counter) for the first 4 Bytes of the hello Random
        @param premature_stop: TRUE if the TLS-Scanner probe had to prematurely stop caused by some limits.
        """
        self.host_name = host_name
        self.previous_results = previous_results
        self.template_percentage_map = template_percentage_map
        self.hello_random_results = hello_random_results
        self.session_random_results = session_random_results
        self.iv_random_results = iv_random_results
        self.complete_random_results = complete_random_results
        self.uses_unix_time = uses_unix_time
        self.premature_stop = premature_stop

    def get_previous_results(self):
        return self.previous_results

    def get_hello_random_results(self):
        return self.hello_random_results

    def get_session_random_results(self):
        return self.session_random_results

    def get_iv_random_results(self):
        return self.iv_random_results

    def get_complete_random_results(self):
        return self.complete_random_results

    def get_unix_time_result(self):
        return self.uses_unix_time

    def get_premature_stop_result(self):
        return self.premature_stop

    def get_template_percentage_map(self):
        return self.template_percentage_map

    def generate_mysql_insert_previous_results(self, database_scheme):
        previous_converted_results = self.convert_previous_results()

        inserter = database_scheme.insert().values(host=self.host_name,
                                                   randomDuplicatesResult=previous_converted_results[0],
                                                   monoBitResult=previous_converted_results[1],
                                                   frequencyResult=previous_converted_results[2],
                                                   runsResult=previous_converted_results[3],
                                                   longestRunBlockResult=previous_converted_results[4],
                                                   fourierResult=previous_converted_results[5],
                                                   templateResult=previous_converted_results[6],
                                                   entropyResult=previous_converted_results[7])

        return inserter

    def generate_mysql_insert_new_results(self, database_scheme):
        dieharder_converted_results = self.convert_new_results()

        inserter = database_scheme.insert().values(host=self.host_name,
                                                   dieharder_0=dieharder_converted_results[0],
                                                   dieharder_1=dieharder_converted_results[1],
                                                   dieharder_2=dieharder_converted_results[2],
                                                   dieharder_3=dieharder_converted_results[3],
                                                   dieharder_13=dieharder_converted_results[4],
                                                   dieharder_14=dieharder_converted_results[5],
                                                   dieharder_15=dieharder_converted_results[6],
                                                   dieharder_16=dieharder_converted_results[7],
                                                   dieharder_17=dieharder_converted_results[8],
                                                   dieharder_100=dieharder_converted_results[9],
                                                   dieharder_101=dieharder_converted_results[10],
                                                   dieharder_102=dieharder_converted_results[11],
                                                   dieharder_200=dieharder_converted_results[12],
                                                   dieharder_201=dieharder_converted_results[13],
                                                   dieharder_202=dieharder_converted_results[14],
                                                   dieharder_203=dieharder_converted_results[15],
                                                   dieharder_204=dieharder_converted_results[16],
                                                   dieharder_205=dieharder_converted_results[17],
                                                   dieharder_206=dieharder_converted_results[18],
                                                   dieharder_207=dieharder_converted_results[19],
                                                   dieharder_208=dieharder_converted_results[20])

        return inserter

    def generate_mysql_insert_misc(self, database_scheme):
        inserter = database_scheme.insert().values(host=self.host_name,
                                                   uses_unix_time=self.uses_unix_time,
                                                   premature_stop=self.premature_stop,
                                                   templateRandom=self.template_percentage_map.get("RANDOM"),
                                                   templateSessionId=self.template_percentage_map.get("SESSION_ID"),
                                                   templateIv=self.template_percentage_map.get("IV"),
                                                   templateComplete=self.template_percentage_map.get("COMPLETE_SEQUENCE"))

        return inserter

    def convert_previous_results(self):
        # Since Python 3.7 dicts are ordered, so this is possible.
        results = []
        for test in self.previous_results:
            test_outcome = self.previous_results.get(test)
            outcome_string = ""
            for outcome in test_outcome:
                outcome_string = outcome_string + outcome + "/"
            results.append(outcome_string)

        return results

    def convert_new_results(self):
        results = []

        for test in self.hello_random_results:
            # Do some simple "flattening"
            # i.e. when there are more "PASSED" than "FAILED", pass the test and set result to "PASSED"
            passed_counter = 0
            failed_counter = 0
            test_result_converted = ""

            hello_results = ""
            if self.hello_random_results is not None:
                hello_results = self.hello_random_results.get(test)
            passed_counter = hello_results.count("PASSED") + hello_results.count("WEAK")
            failed_counter = hello_results.count("FAILED")

            if failed_counter > passed_counter:
                test_result_converted = test_result_converted + "RANDOM" + "/"

            session_results = ""
            if self.session_random_results is not None:
                session_results = self.session_random_results.get(test)
            passed_counter = session_results.count("PASSED") + session_results.count("WEAK")
            failed_counter = session_results.count("FAILED")

            if failed_counter > passed_counter:
                test_result_converted = test_result_converted + "SESSION_ID" + "/"

            iv_results = ""
            if self.iv_random_results is not None:
                iv_results = self.iv_random_results.get(test)
            passed_counter = iv_results.count("PASSED") + iv_results.count("WEAK")
            failed_counter = iv_results.count("FAILED")

            if failed_counter > passed_counter:
                test_result_converted = test_result_converted + "IV" + "/"

            complete_result = ""
            if self.complete_random_results is not None:
                complete_result = self.complete_random_results.get(test)
            passed_counter = complete_result.count("PASSED") + complete_result.count("WEAK")
            failed_counter = complete_result.count("FAILED")

            if failed_counter > passed_counter:
                test_result_converted = test_result_converted + "COMPLETE_SEQUENCE"

            results.append(test_result_converted)

        return results
