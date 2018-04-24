import string
import sys

'''
Write contents to file
Default is per_line and mode is 'w'
'''
def write_file(name=None, contents=[], per_line=True, mode="w", add_newline=True, no_encode=False, append_newline=False):
    if name:
        
        name = sys.prefix + '/' + name

        f = open(name, mode)
        string = ""
        for content in contents:
            if append_newline:
                content = content + '\n'
            if per_line:
                if no_encode:
                    f.write(content)
                else:
                    f.write(content.encode('utf-8'))
                if add_newline:
                    f.write("\n")
            else:
                string = string + content

        if not per_line:
            f.write(string)

        f.close()
    
    return None

'''
Returns contents of a file
Can specify start and end of contents in reading a file
'''
def read_file(name=None, start=None, end=None, strip=False, dict_format=False, decode=False):
    if name:

        name = sys.prefix + '/' + name
        
        f = open(name, "r")
        contents = []
        dictionary = {}
        for line in f:
            if strip:
                line = line.strip()
            splitted = line.split(" ")
            dictionary[splitted[0]] = splitted[1:]
            if decode:
                line = line.decode('utf-8')
            contents.append(line)

        f.close()
        if start is not None:
            contents = contents[start:]

        if dict_format:
            return dictionary

        return contents
    return None


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
	term = term.replace('o', 'u')
	term = term.replace('e', 'i')
	return term in dictionary