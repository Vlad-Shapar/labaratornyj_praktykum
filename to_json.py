import json
from bank import nounlist2
from kurs import nounlist1

def  convertToJSON():
 with open("kurs.json", 'w') as write_file:
    json.dump(nounlist1, write_file)
def convertInJSON():
 with open("bank.json", 'w') as write_file:
    json.dump(nounlist1, write_file)