
from collections import defaultdict

def split_in_n(string, n=2):
    l = []
    duet = ''

    for j in range(0,n, 2):
        for i, c in enumerate(string[j:]):
            duet = duet + c
            if i % n == n-1:
                l.append(duet)
                duet = ''

    return l

def odds():
    return {
        'a': 1
    }

def conversion_dict():
    return {
        'ac': 'a',
        'qs': 'y',
        #'8c': 'w',
        'ad': ' ', 
        'kh': '\n',
        #'kh': ' ',
        'ah': '0',
        '2h': '1',
        '3h': '2',
        '4h': '3',
        '5h': '4',
        '6h': '5',
        '7h': '6',
        '8h': '7',
        '9h': '8',
        'th': '9',
        #'2d': '.',
        'td': '-',
        '4D': '[',
        '5D': ']',
        '2D': '<',
        '3D': '>',

        'ac': 'a',
        '2c': 'b',
        '3c': 'c',
        '4c': 'd',
        '5c': 'e',
        '6c': 'f',
        '7c': 'g',
        '8c': 'h',
        '9c': 'i',
        'tc': 'j',
        'jc': 'k',
        'qc': 'l',
        'kc': 'm',

        'as': 'n',
        '2s': 'o',
        '3s': 'p',
        '4s': 'q',
        '5s': 'r',
        '6s': 's',
        '7s': 't',
        '8s': 'u',
        '9s': 'v',
        'ts': 'w',
        'js': 'x',

        'ks': 'z',
        'jh': '\'',
        '2d': '.',
        '3d': ',',
        '4d': '?',
        '5d': ':',
        '6d': ';',
        '7d': '!',
        '8d': '(',
        '9d': ')',
    }


# Now it doesn't work with chars in caps..
def replace_(changes, pair):
    f,s = pair[0], pair[1]

    if s.lower() == 's' or s.lower() == 'c':
        if pair.lower() in changes.keys():
            res = changes[pair.lower()]
            if s.isupper():
                res = res.upper()
        else:
            #res = '[' + pair + ']'
            res = '_' + pair + '_'

    else:
        if pair in changes.keys():
            res = changes[pair]
        else:
            res = pair

    return res

def replace(l, changes):
    return map(lambda x: replace_(changes, x), l)


def find_ocurrences(l):
    ocurrences = defaultdict(int)

    for item in l:
        ocurrences[item] += 1

    s_ocurrences = sorted([(a, b) for a,b in ocurrences.items()], key=lambda x: x[1])
    return (ocurrences, s_ocurrences)

def get_words(cypher, space_duet='ad'):
    c = replace(cypher, {space_duet: ' '})
    c = ''.join(c).split()
    return c

def words_more_popular_in_cypher(cypher, space_duet='ad'):
    c = get_words(cypher, space_duet)
    (oc, s_oc) = find_ocurrences(c)
    return s_oc

def words_with_double_letter(text):
    l = []

    for word in text.split(' '):
        if '__' in word:
            if word not in l:
                l.append(word)

    return l

def first_letter_oc(cypher):
    w = get_words(cypher)
    first_letters = map(lambda x: x[0:2], w)
    (_, s_oc) = find_ocurrences(first_letters)

    return s_oc

def get_rid_of_ay(text):
    return ' '.join(map(lambda x: x[:-2] if (x[-2:].lower()) == 'ay' else x, text.split(' ')))

    text.split()
def decrypt():
    with open('Alteryx_CUHack2017.txt') as f:
        cypher = f.read()
        cypher = cypher[0:-1]

    pairs = split_in_n(cypher, 2)
    #oc, s_oc = find_ocurrences(map(lambda x: x.lower(), pairs))
    #print(s_oc)
    #print(len(s_oc))
    updated = replace(pairs, conversion_dict())
    updated = ''.join(updated)
    #updated = get_rid_of_ay(updated)

    print(updated)

    #print(words_more_popular_in_cypher(pairs))
    #print(first_letter_oc(pairs))
    #print(len(first_letter_oc(pairs)))

def __main__():
    decrypt()

__main__()

