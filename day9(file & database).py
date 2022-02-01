'''
csv
'''

import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
	]
with open('villains', 'wt') as fout: # context manager
    csvout = csv.writer(fout)
    csvout.writerows(villains)

with open('villains', 'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin] #list comprehension

print(villains)

import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)

import csv
villains = [
	{'first':'Doctor', 'last': 'No'},
	{'first':'Rosa', 'last': 'Klebb'},
	{'first':'Mister', 'last': 'Big'},
	{'first':'Auric', 'last':'Goldfinger'},
	{'first':'Ernst', 'last':'Blofeld'},
	]
with open('villains.txt', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

import csv
with open('villains.txt', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)

'''
xml : markup
Using : data feed, sending message
Pasing By Using ElementTree module
'''

#import xml.etree.ElementTree as et
#tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
root.tag