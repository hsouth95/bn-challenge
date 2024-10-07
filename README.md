# Bright Networks Technical Test

A recommendation engine for members looking for roles.


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