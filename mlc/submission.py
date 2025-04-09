from mlc.birdclef import ScorableModelTemplate

class ScorableModel(ScorableModelTemplate):

    def predict(self, raw_files: list[str]):
        """Input argument will vary. See you competition's template.

        :param raw_files: list of file path strings, depends on competition
        :return predictions: dataframe or np.array, depends on competition
        """
        # Implement this: may return random predictions for the first assignment
        raise NotImplementedError()

    def process_inputs(self, raw_files: list[str]):
        """Input argument will vary. See you competition's template.

        :param raw_files: list of file path strings, depends on competition
        :return: anything needed for you model to make predictions, e.g. features or processed data
        """
        # Implement this: only need to read in files for first assignment
        raise NotImplementedError()

# Intialize, runs: __check_rep__ to validate class
model = ScorableModel() # error will be raised if the above is not implemented correctly