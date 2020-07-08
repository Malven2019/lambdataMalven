# lambdataMalven
 Contains file for upload on the package index

The repository contains a function to detect duplicate columns and the other one that coverts State abbreviation to full name and vice versa
e.g FL - Florida etc

##Installation
Git clone and navigate to the repo from your command-line:

##Usage
```
git clone REMOTE_ADDRESS
cd /path/to/repo
The code finds duplicate columns within the DataFrame
The code converts the State abbreviation to full name and vice versa.
````
Create/activate a virtual environment
```
pipenv --python 3.7
pipenv install  # installs all  packages inside the Pipfile
pipenv shell
```
Run example script:
```
python -m Duplicate
python -m City
```
