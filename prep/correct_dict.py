from copy import deepcopy
from utilities import write_file, read_file


'''
Writes to a file the entries with the specified tags
'''
def find_entries(tag=None, dest=None, add_tag=True):
	if tag:
		contents = read_file('data/cebposdict-nc.txt', strip=True, dict_format=True)
        found_entries = []
        for key, val in sorted(contents.iteritems()):
            if tag in val:
                if add_tag:
                    val.insert(0, key)
                    found_entries.append(' '.join(val) + '\n')
                else:
                    found_entries.append(key + '\n')

		write_file('data/' + dest, contents=found_entries, add_newline=False)

'''
Corrects NUM
'''
def correct_NUM():
    contents = read_file('data/old-NUM.txt', strip=True, dict_format=True)
    entries = read_file('data/cebposdict-nc.txt', strip=True, dict_format=True)

    for content in contents:
        entries[content] = ['NUM']

    write_file('data/cebposdict-nc.txt', contents=[''], add_newline=False, mode='w')
    for key, value in sorted(entries.iteritems()):
        new_entry = [key + ' ']
        value = list(set(value))
        new_entry.append(' '.join(value))
        new_entry.append('\n')
        write_file('data/cebposdict-nc.txt', contents=new_entry, add_newline=False, mode='a')
        new_entry = []

'''
Corrects OTH
'''
def correct_OTH():
    contents = read_file('data/new-OTH.txt', strip=True, dict_format=True)
    entries = read_file('data/cebposdict-nc.txt', strip=True, dict_format=True)

    for key, value in contents.iteritems():
        if 'REM' in value:
            if key in entries:
                del entries[key]
        else:
            entries[key] = value

    if len(contents):
        write_file('data/cebposdict-nc.txt', contents=[''], add_newline=False, mode='w')
        for key, value in sorted(entries.iteritems()):
            new_entry = [key + ' ']
            value = list(set(value))
            new_entry.append(' '.join(value))
            new_entry.append('\n')
            write_file('data/cebposdict-nc.txt', contents=new_entry, add_newline=False, mode='a')
            new_entry = []

'''
Corrects ADV
'''

def correct_ADV():
    contents = read_file('data/new-ADV.txt', strip=True, dict_format=True)
    entries = read_file('data/cebposdict-nc.txt', strip=True, dict_format=True)

    for key, value in contents.iteritems():
        if 'REM' in value:
            if key in entries:
                del entries[key]
        else:
            entries[key] = value

    if len(contents):
        write_file('data/cebposdict-nc.txt', contents=[''], add_newline=False, mode='w')
        for key, value in sorted(entries.iteritems()):
            new_entry = [key + ' ']
            value = list(set(value))
            new_entry.append(' '.join(value))
            new_entry.append('\n')
            write_file('data/cebposdict-nc.txt', contents=new_entry, add_newline=False, mode='a')
            new_entry = []
'''
Removes function words from the dictionary
'''
def remove_function_words():
    entries = read_file('data/cebposdict-nc.txt', strip=True, dict_format=True)

    function_tags = ['DET', 'PART', 'CONJ', 'PRON']
    function_words = {
        'DET': [],
        'PART': [],
        'CONJ': [],
        'PRON': []
    }

    for tag in function_tags:
        for key, value in entries.iteritems():
            if tag in value:
                value.append('REM')
                function_words[tag].append(key)
    write_file('data/cebposdict-nc.txt', contents=[''], add_newline=False, mode='w')
    for key, value in sorted(entries.iteritems()):
        if 'REM' not in value:
            new_entry = [key + ' ']
            value = list(set(value))
            new_entry.append(' '.join(value))
            new_entry.append('\n')
            write_file('data/cebposdict-nc.txt', contents=new_entry, add_newline=False, mode='a')
            new_entry = []

    for key, value in function_words.iteritems():
        write_file('data/' + key + '.txt', contents=value, add_newline=False, append_newline=True, mode='w')

'''
Transforms all entries to lowercase
'''
def entries_to_lowercase():
	entries = read_file('data/cebposdict-nc.txt', strip=True, dict_format=True)
	entries_copy = deepcopy(entries)

	for key, value in entries.iteritems():
		if key[0].isupper():
			entries_copy[key.lower()] = entries_copy.pop(key)

	write_file('data/cebposdict-nc.txt', contents=[''], add_newline=False, mode='w')
	for key, value in sorted(entries_copy.iteritems()):
		new_entry = [key + ' ']
		value = list(set(value))
		new_entry.append(' '.join(value))
		new_entry.append('\n')
		write_file('data/cebposdict-nc.txt', contents=new_entry, add_newline=False, mode='a')
		new_entry = []


if __name__ == "__main__":
	# correct_ADV()
	# find_entries(tag='ADV', source='pos-dictionary.txt', dest='new/ADV.txt')
    # correct_NUM()
    # correct_OTH()
    # remove_function_words()
	# entries_to_lowercase()
    pass
