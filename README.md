# Bright Networks Technical Test

A recommendation engine for matching members to their perfect jobs.

## Setup

This project primarily uses [poetry](https://python-poetry.org/) as the dependency management software.

To install dependencies with poetry run the following commands

```bash
poetry install --no-root
poetry shell
```

This will put you in a virtualenv with all the dependencies installed.

Alternatively, if you don't want to utilise poetry, there is a requirements.txt file that you can create a virtualenv of to run the code, as shown below:

```bash
virtualenv .venv
pip install -r requirements.txt
```

We now need to install pre-trained models for our project (explained further down as to why it's used).

```bash
python -m spacy download en_core_web_sm
```

## Running the project

From either a poetry shell or a virtualenv. Run the following:

```bash
python src/main.py
```

## Running tests

From either a poetry shell or a virtualenv. Run the following:

```bash
python -m pytest
```

# Thoughts about the project

## Thoughts of the project and my approach

I enjoyed this challenge as I felt the data provided gave a number of ways to overcome the challenge. My focus was on getting the **perfect** match (location AND role)
and so my approach involved a simpler matching algorithm instead of an alternative strategy of scoring matches (e.g. You wanted Leeds but the job role matches). I also wanted to make it quite an open solution to allow more custom biographies to be entered.

One of my first thoughts was to write some regex to filter the language provided in the example datasets. However, I felt this would be too restrictive and would mostly result on default answers when any biography was expanded upon.
I initially went with using Scapy thinking I could use the 'Named entity recognition' to get both locations and job roles. However, with my limited experience of NLPs, I struggled to get the job roles identified. I think with more
time I could write some custom logic around the usage of nouns to match these.

I struggled to get the 'negative' matching of locations without adding rather restrictive checks. If I had more time i'd like to expand these checks to look at the context of the locations mentioned and try to determine if it's a negative sentiment which might suggest that they did not want to work there. Additionally, with the job roles, I did not get around to fuzzy matching these (e.g. Marketing wouldn't match a Marketer in my solution). Given the time I'd look into text matching for similarities in order to overcome this.

Looking back I'd adjust the structure of my code to allow separate extractors using an Abstract Base Class to ensure basic functionality from the calling code. You could then register these extractors against a 'search' criteria in order to allow further fields that you may want to search on (e.g. seniority). This would also allow for better logic separation as right now the code melds a bit too much with the differing logic of location vs. job role.

## Smaller things I'd improve on if I had more time

* Add arguements for `main.py` to allow overriding endpoints - this is easily done with `argparse` or `typer` but didn't want to focus too much time on it.
* Add the ability for alternative formats for data entry - e.g. JSON file on disk
* Add more tests for the `Matcher` class - this was a much simpler class so wanted to focus on `Extractor` testing
* Add async HTTP calls for the data requests - this could allow for better performance by running the requests in parallel, important if the datasets were to increase in size.
* Update the `Extractor` class to better use the `nlp` loading. I think loading from the `bio` field lends itself to a caching opportunity and if the dataset were to increase in size, this would need to be utilised.
* Add pre-hooks (`pre-commit`) in order to add basic automated formatting and even pre-commit/push testing