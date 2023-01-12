# Website and Domain references extractor
These python scripts allow you to extract list all domains or links that a certain website refers to. 

## Required python modules
This script requires the following python modules:
* Beautiful Soup 4
* requests
* urlib (only required for DomainExtract.py)

## Usage
* Just launch the python script like this: ./python3 LinkExtract.py
* Then give it the address of a website you want to check eg. "https://www.wp.pl".
* The script will save every found url or domain to a .txt file.
