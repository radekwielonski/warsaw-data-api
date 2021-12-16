from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Warsaw data python api"
LONG_DESCRIPTION = "Package which provides pythonic way to use Warsaw data API"

# Setting up
setup(
    name="warsaw-data-api",
    version=VERSION,
    author="Radoslaw Wielonski",
    author_email="<radek.wielonski@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=[],
    keywords="python, UM Warszawa, warsaw data api",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License" "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "warsaw-data-api=warsaw_data_api:main",
        ]
    },
)
