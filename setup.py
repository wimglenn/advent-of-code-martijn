import glob
from setuptools import setup

setup(
    name="advent-of-code-martijn",
    author="Martijn Pieters",
    version="0.1",
    url="https://github.com/mjpieters/adventofcode",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=["nbformat", "advent-of-code-data"],
    python_requires=">= 3.7",
    packages=["plugin"],
    package_data={"plugin": ["2017/*.ipynb", "2018/*.ipynb"]},
    entry_points={"adventofcode.user": ["martijn = plugin:main"]},
)
