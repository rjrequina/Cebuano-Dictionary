import os
import string
import nltk
from utilities import write_file, read_file


'''
Parse dictionary into following format:

word tag1 tag2
'''
def parse_raw():
    contents = read_file('data/raw.txt')
    printable = set(string.printable)
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    new_entry = True
    entry_count = 1
    add_entry = False
    get_next = False
    entries = []
    dict_entry = ''

    for idx, content in enumerate(contents):
        content = filter(lambda x: x in printable, content)
        if not content.strip() == '$':
            dict_entry += content.strip() + ' '
        else:
            tokens = dict_entry.split(' ')

            # Will not include entries that are affixes
            # They starts with -
            if not tokens[0].startswith('-'):

                start = 1
                # The first token is the entry
                # If the first token starts with '*', it means the entry cannot standalone without the prefix
                # The prefix is the next token
                # If the first token ends with ',', it means it has an alternative entry
                # The next token is the alternative entry
                entry = tokens[0]
                alternative_entry = ''
                if entry.startswith("*"):
                    entry = entry.replace('*', '')
                    prefix = tokens[1]
                    prefix = prefix.replace('-', '')
                    entry = prefix + entry
                    # Increment start when prefix is the necessary for the entry
                    start += 1

                if entry.endswith(','):
                    entry = entry.replace(',', '')
                    alternative_entry = tokens[1]

                    # Increment start when there is an alternative entry
                    start += 1

                # Start to get the root tags of the entry
                # Including the equivalent terms
                tags = {
                    'n': 'NOUN',
                    'adj': 'ADJ',
                    'v': 'VERB',
                    'gen.': 'PRON',
                    'gen': 'PRON',
                    'abbreviation': 'NOUN',
                    'particle': 'PART',
                    'p': 'PART',
                    'number': 'NUM',
                    'numeral': 'NUM',
                    'interrogative': 'PRON',
                    'a': 'ADJ'
                }

                idx = start
                details = []
                while idx < len(tokens):
                    curr = tokens[idx]

                    if curr in tags:
                        # If the previous or succeeding token does not starts or ends with '-',
                        # It means that the tag is a root tag.
                        # Otherwise, the tag is derived tag using the affixes
                        is_left_affix = tokens[idx - 1].startswith('-') or tokens[idx - 1].endswith('-')
                        is_right_affix = tokens[idx + 1].startswith('-') or tokens[idx + 1].endswith('-')
                        if  not is_left_affix and not is_right_affix:
                           if curr == 'a':
                               # Checks if the surrounding words are english words.
                               # If yes, the curr word is not an adjective tag
                               # It is a article
                               surrounding_words = [tokens[idx - 1], tokens[idx + 1]]
                               text_vocab = set(w.lower() for w in surrounding_words if w.lower().isalpha())
                               difference = list(text_vocab.difference(english_vocab))
                               if len(difference) == 0:
                                   details.append(tags[curr])
                           else:
                               details.append(tags[curr])

                    elif curr == 'see' or curr == '=':
                        is_right_affix = tokens[idx + 1].startswith('-') or tokens[idx + 1].endswith('-')
                        if not is_right_affix:
                            details.append('=')
                            tokens[idx + 1] = tokens[idx + 1].replace('*', '')
                            tokens[idx + 1] = tokens[idx + 1].replace('.', '')
                            tokens[idx + 1] = tokens[idx + 1].replace(',', '')
                            details.append(tokens[idx + 1])

                    idx += 1


            entry = entry + ' ' + ' '.join(details) + '\n'
            entries.append(entry)
            if len(alternative_entry):
                alternative_entry = alternative_entry + ' ' + ' '.join(details) + '\n'
                entries.append(alternative_entry)
            dict_entry = ''

    write_file('data/cebposdict-1.txt', contents=entries, no_encode=True, add_newline=False)
    print('parse_raw: Finished!')

'''
Remove entries with no POS tags
'''
def remove_no_pos_tags():
    entries = read_file('data/cebposdict-1.txt')
    no_tags = []
    others = []

    num = 1
    for entry in entries:
        words = nltk.word_tokenize(entry)
        if len(words) <= 1:
            no_tags.append(entry)
        else:
            others.append(entry)

    write_file('data/cebposdict-2.txt', contents=others, no_encode=True, add_newline=False, mode='w')
    print('remove_no_pos_tags: Finished!')

'''
Resolve duplicate entries
'''
def resolve_duplicate_entries():
    entries = read_file('data/cebposdict-2.txt')
    result = {}

    for outer_idx, entry in enumerate(entries):
        words = nltk.word_tokenize(entry)

        if words[0] not in result:
            result[words[0]] = []
            result[words[0]] = " ".join(list(words))
        else:
            value = " ".join(list(words[1:]))
            result[words[0]] = result[words[0]] + ' ' + value
    
    write_file('data/cebposdict-3.txt', contents=sorted(result.values()), add_newline=False, append_newline=True)
    print('resolve_duplicate_entries: Finished!')

'''
Resolves = in entries
'''
def resolve_equals():
    write_file('data/cebposdict-4.txt', contents=[''], no_encode=True, add_newline=False, mode='w')
    entries = read_file('data/cebposdict-3.txt', dict_format=True)
    result = []
    for key, value in entries.iteritems():
        words = nltk.word_tokenize(" ".join(value))
        new_entry = [key + ' ']
        related_words = []
        for word in words:
            if word in ['PART', 'ADJ', 'PRON', 'VERB', 'NOUN', 'NUM']:
                new_entry.append(word + ' ')
            elif word != '=':
                related_words.append(word)

        for rel_word in related_words:
            if rel_word in entries:
                values = entries[rel_word]
                words = nltk.word_tokenize(" ".join(value))
                # words = list(Text(" ".join(values)).words)
                for word in words:
                    if word in ['PART', 'ADJ', 'PRON', 'VERB', 'NOUN', 'NUM']:
                        new_entry.append(word + ' ')

        new_entry.append('\n')
        write_file('data/cebposdict-4.txt', contents=new_entry, add_newline=False, mode='a')
        new_entry = []

    print('resolve_equals: Finished!')

'''
Remove entries with no POS tags phase 2
'''
def remove_no_pos_tags_2():
    entries = read_file('data/cebposdict-4.txt')
    no_tags = []
    others = []

    num = 1
    for entry in entries:
        words = nltk.word_tokenize(entry)
        if len(words) <= 1:
            no_tags.append(entry)
        else:
            others.append(entry)

    write_file('data/cebposdict-5.txt', contents=sorted(others), add_newline=False, mode='w')
    print('remove_no_pos_tags_2: Finished!')

'''
Resolve duplicate tags per entry
'''
def resolve_duplicate_tags():
    write_file('data/cebposdict-nc.txt', contents=[''], no_encode=True, add_newline=False, mode='w')
    entries = read_file('data/cebposdict-5.txt', dict_format=True, strip=True)
    result = []
    new_entry = []
    contents = []
    for key, value in sorted(entries.iteritems()):
        new_entry = [key + ' ']
        value = list(set(value))
        new_entry.append(' '.join(value))
        new_entry.append('\n')
        contents.append(new_entry)
        write_file('data/cebposdict-nc.txt', contents=new_entry, add_newline=False, mode='a')
        new_entry = []

    print('resolve_duplicate_tags: Finished!')


def main():
    parse_raw()
    remove_no_pos_tags()
    resolve_duplicate_entries()
    resolve_equals()
    remove_no_pos_tags_2()
    resolve_duplicate_tags()


if __name__== "__main__":
    main()
