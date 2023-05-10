import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")


def get_version():
    init = open(os.path.join(ROOT, "warsaw_data_api", "__init__.py")).read()
    return VERSION_RE.search(init).group(1)


DESCRIPTION = "Warsaw data python api"
LONG_DESCRIPTION = "Package which provides pythonic way to use Warsaw data API"

# Setting up
setup(
    name="warsaw-data-api",
    version=get_version(),
    author="Radoslaw Wielonski",
    author_email="<radek.wielonski@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=["requests"],
    setup_requires=["requests"],
    keywords="python, UM Warszawa, warsaw data api, ztm, public transport",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "warsaw-data-api=warsaw_data_api:main",
        ]
    },
)
