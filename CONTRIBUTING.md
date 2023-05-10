# Welcome to Warsaw Data Api contributing guide

Thank you for investing your time in contributing to my project!

## Getting started

### Issues

#### Create a new issue

If you found problem or have a feature request for the package search if an issue already exists. If a related issue doesn't exist, you can open a new one.

#### Solve an issue

If you find an issue you would like to work on, you are welcome to open a PR with a fix.

### How to make a change

1. Fork the repository
2. Make the changes
3. Run the automatic tests

```sh
$ pip install -r requirements.txt
```

```sh
$ python -m unittest
```

4. Install package locally and manually check your changes

```
python setup.py install
```

5. Don't forget to have pre-commit hooks installed

```sh
$ pip install pre-commit && pre-commit install
```

6. Commit your changes (in conventional commit convention) and create a PR.
