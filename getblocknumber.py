
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

## Getting the amount of coins in existance
coins = new['result']['coins']

## String coins variable
coins = str(coins)

## Printing coins variable
print 'Amount of coins: ' + coins

## Printing blocks variable
print 'Block Number: ' + blocks
