
## Importing required modules
import json
import subprocess


## Getting the data
mining = subprocess.check_output("curl -X GET --header 'Accept: application/json' 'http://api.maxcoinhub.io/Blockchain/GetMiningInfo'", shell=True)

#print mining

## Converting the string to JSON Format
new = json.loads(mining)

#print new

## Getting the latest block
blocks = new['result']['blocks']

## Stringing blocks variable
blocks = str(blocks)

## Printing blocks variable
print 'Block Number: ' + blocks
