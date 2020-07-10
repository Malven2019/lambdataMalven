# setup.py file
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="LAMBDATAMALVEN",  # the name that you will install via pip
    version="1.0",
    author="Malven Mtombeni",
    author_email="malmtombeni@gmail.com",
    description="The Set up file",
    long_description=long_description,
    # required if using a md file for long desc
    long_description_content_type="text/markdown",
    #license="MIT",
    url="https://github.com/Malven2019/LambdataMalven",
    #keywords="",
    packages=['lambdata'] #find_packages()  # ["lambdata"]
)
