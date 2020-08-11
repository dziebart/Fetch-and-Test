

class StatisticalResults:

    def __init__(self, previous_results, template_percentage_map,
                 hello_random_results, session_random_results, iv_random_results,
                 complete_random_results, uses_unix_time, premature_stop):
        """
        Creates a wrapper object, which holds the previous results from the TLS-Scanner RNG-Probe and the new results
        from the Dieharder test-battery using dicts. In addition to that, this class also holds two boolean values
        related to the behaviour and scanning procedure of the scanned host. This class acts as a wrapper for all these
        values, so the "slave" can return all required results to the "master" in one method.
        @param previous_results: dict containing the test results from the TLS-Scanner RNG-Probe
        @param template_percentage_map: dict containing the template test results from the TLS-Scanner RNG-Probe
        @param hello_random_results: dict containing the results from the dieharder tests on the serverHello randoms
        @param session_random_results: dict containing the results from the dieharder tests on the sessionIDs
        @param iv_random_results: dict containing the results from the dieharder tests on the initialization vectors
        @param complete_random_results: dict containing the results from the dieharder tests on the complete sequence
        @param uses_unix_time: TRUE if the host uses unixTime (or counter) for the first 4 Bytes of the hello Random
        @param premature_stop: TRUE if the TLS-Scanner probe had to prematurely stop caused by some limits.
        """
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
