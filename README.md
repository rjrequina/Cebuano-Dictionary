# Cebuano-Dictionary
Cebuano Dictionary based on John Wolff's 'A dictionary of Cebuano Visayan'

## Installation
* `pip install cebdict` or
* inside the folder run `python setup.py install`

## Functions
* search()
   - Accepts a Cebuano word and returns the POS tags of that word
* is_entry()
   - Accepts a Cebuano word and checks if the word exists in the dictionary
   
## How to Use
```
from cebdict import dictionary

print(dictionary.search('buang'))
Output: ['ADJ']

print(dictionary.is_entry('buang'))
Output: True
```
