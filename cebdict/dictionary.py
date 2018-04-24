import string
from utilities import read_file


'''
Get the dictionary entries
'''
def get_entries():
	entries = read_file(name='data/cebposdict.txt', strip=True, dict_format=True)

	func_words = ['CONJ', 'DET', 'PART', 'PRON']

	for func in func_words:
		words = read_file(name='data/function_words/' + func + '.txt', strip=True)

		for word in words:
			if word in entries:
				entries[word].append(func)
			else:
				entries[word] = [func]

	return entries



dictionary = get_entries()


'''
Search term in dictionary
'''
def search(term=''):
	term = term.lower()
	if term not in dictionary:
		term = term.replace('o', 'u')
		term = term.replace('e', 'i')

	if term not in dictionary:
		return None

	return dictionary[term]


'''
Checks if the term exists in the dictionary
'''
def is_entry(term=''):
	term = term.lower()
	term = term.replace(term, 'o', 'u')
	term = term.replace(term, 'e', 'i')
	return term in dictionary