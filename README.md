# ML Competitions: Models & Scoring

## Repository Instructions

This is the base repository to build upon.

1. Fork this repository
2. Ensure your repository is set to private
3. Add @ryanhammonds and @ustunb to the repository
4. Add all team members to the respository

Then install the repostory code in your environment:

```bash
git clone https://github.com/{your fork}/mlc.git
pip install -e mlc
```

## Submission Template Instructions

There is `ScorableModelTemplate` class and `compute_score` function
for each comptition, accessible from:

- `mlc/birdclef.py`
- `mlc/bugnist.py`
- `mlc/cashflow.py`

Extend the `ScorableModelTemplate` and include your work. The `.process_inputs` and `.predict`
methods need to be implemented, and have specific required inputs. These inputs are documented
in `ScorableModelTemplate.predict` and `ScorableModelTemplate.process_inputs` for each competition.
In BugNIST and BirdCLEF, these functions require a list of file paths to each tif or ogg file.
Cashflow reqiures two inputs, string paths to consumer_data.parquet and transactions.parquet.

The `.process_inputs` method should:

1) Read in raw data
2) Compute features (optional for the first assignment)
3) Be called from `.predict`

The `.predict` method should:

1) Call `.process_inputs` to read in data and compute features
2) Pass computed features to trained, e.g. pytorch or sklearn, model
3) Return predictions that are compatible with you competitions `compute_score` function.

Each competition has a specific `compute_score` function. Check it to ensure what is
returned from `.predict` is compatiable. The each `ScorableModelTemplate` class has
a `__check_rep__` method that tests you predictions with the scoring function. See the
`__check_rep__` method for an example of how to pass the output from `.predict` to `compute_score`.

Complete the following and commit it to a submission.py or submission.ipynb file:

```python
from mlc.[your competition] import ScorableModelTemplate

class ScorableModel(ScorableModelTemplate):

    def predict(self, raw_files: list[str]):
        """Input argument will vary. See you competition's template.

        :param raw_files: list of file path strings
        :return predictions: dataframe with columns: "row_id" and a each of the 206 class names
        """
        # Implement this: may return random predictions for the first assignment
        raise NotImplementedError()

    def process_inputs(self, raw_files: list[str]):
        """Input argument will vary. See you competition's template.

        :param raw_files: list of file path strings
        :return: anything needed for you model to make predictions, e.g. features or processed data
        """
        # Implement this: only need to read in files for first assignment
        raise NotImplementedError()

model = ScorableModel() # error will be raised if the above is not implmented correctly
```

## Competition Submission Form

Once the above is completed, submit the [Competition Submission Form](https://forms.gle/giucmSFyYQiBjL1S6).
