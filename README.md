# Cebuano-Dictionary
Cebuano Dictionary based on John Wolff's 'A dictionary of Cebuano Visayan'


Number of entries |
--- |
16587 |


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

## References

* Wolff, J. (1972). A dictionary of Cebuano Visayan (Vol. 1). Cornell University, 
       Southeast Asia Program and Linguistic Society of the Philippines.

* Wolff, J. (1972). A dictionary of Cebuano Visayan (Vol. 2). Cornell University,  
                  Southeast Asia Program and Linguistic Society of the Philippines.
