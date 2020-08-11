
class StatisticalResults:

    def __init__(self, previous_results, template_percentage_map,
                 hello_random_results, session_random_results, iv_random_results,
                 complete_random_results, uses_unix_time, premature_stop):
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
