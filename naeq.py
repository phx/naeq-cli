#!/usr/bin/env python3

import json, os, sys

SAVE = False
SILENT = False
PERSONAL = True
pdict = 'personal_dictionary.json'
liber_al = 'liber_al.json'

if not os.path.exists(pdict):
    with open(pdict, 'w') as f:
        f.write('{}')

ceb = {
      "a": 1,"b": 20,"c": 13,"d": 6,"e": 25,"f": 18,"g": 11,"h": 4,"i": 23,"j": 16,"k": 9,
      "l": 2,"m": 21,"n": 14,"o": 7,"p": 26,"q": 19,"r": 12,"s": 5,"t": 24,"u": 17,"v": 10,
      "w": 3,"x": 22,"y": 15,"z": 8
      }

# Get arguments or piped input:
if len(sys.argv) <= 1:
    try:
        phrase = ' '.join([c for c in sys.stdin.readlines()])
        phrase = phrase.strip()
        try:
            phrase = int(phrase)
        except:
            pass
    except:
        print('must take arguments or pipe from stdin')
elif len(sys.argv) > 1:
    if sys.argv[1] == '-s':
        phrase = ' '.join(sys.argv[2:])
        SAVE = True
    elif sys.argv[1] == '-ss':
        phrase = ' '.join(sys.argv[2:])
        SAVE= True
        SILENT = True
    elif sys.argv[1] == '-np':
        phrase = ' '.join(sys.argv[2:])
        SAVE=False
        PERSONAL = False
    else:
        phrase = ' '.join(sys.argv[1:])
    phrase = phrase.strip()
    try:
        phrase = int(phrase)
    except:
        pass

values = []

# Get values from CEB:
if isinstance(phrase, str):
    for ch in phrase.lower():
        if ch in ceb:
            values.append(ceb[ch])
    value = str(sum(values))
elif isinstance(phrase, int):
    value = str(phrase)
else:
    print('Error getting value from phrase.')
    sys.exit()

if isinstance(phrase, str):
    phrase = phrase.upper()

# Output:
print('===============================================================')
print('PHRASE: ' + str(phrase))
print('AEQ VALUE: ' + value)

# Get values from personal dictionary:
if PERSONAL:
    try:
        with open(pdict, 'r') as jdata:
            data = json.load(jdata)
            if value in data.keys():
                print('===============================================================')
                print('PERSONAL MATCHES:')
                print('---------------------------------------------------------------')
                for line in data[value]:
                    print(line)
    except: pass

if not SILENT:
    print('===============================================================')
    print('NAEQ MATCHES:')
    print('---------------------------------------------------------------')
    # Get values from naeq:
    with open(liber_al, 'r') as jdata:
        naeq = json.load(jdata)
        if value in naeq.keys():
            for line in naeq[value]:
                print(line)

print('===============================================================')


def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item


def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))


# Write new query to personal dictionary json object:
if SAVE:
    try:
        with open(pdict, 'r') as jdata:
            data = json.load(jdata)
            if value in data.keys():
                new_values = list(data[value])
                new_values.append(phrase)
                new_values = sort_and_deduplicate(new_values)
                data.update({value : new_values})
                with open(pdict, 'w') as jdata:
                    jdata.write(json.dumps(data))
            else:
                data.update({value : [phrase]})
                with open(pdict, 'w') as jdata:
                    jdata.write(json.dumps(data))
    except: pass
