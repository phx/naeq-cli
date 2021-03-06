#!/usr/bin/env python3

import json, os, shutil, sys

SAVE = False
SILENT = False
PERSONAL = True
DELETE = False
QUERY = False
pdict = 'dictionary.json'
backup = 'dictionary.bak'
liber_al = 'liber_al.json'

if not os.path.exists(pdict):
    with open(pdict, 'w') as f:
        f.write('{"0": []}')

ceb = {
      "a": 1,"b": 20,"c": 13,"d": 6,"e": 25,"f": 18,"g": 11,"h": 4,"i": 23,"j": 16,"k": 9,
      "l": 2,"m": 21,"n": 14,"o": 7,"p": 26,"q": 19,"r": 12,"s": 5,"t": 24,"u": 17,"v": 10,
      "w": 3,"x": 22,"y": 15,"z": 8,
      "0": 0,"1": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9
      }

# Get arguments or piped input:
if len(sys.argv) <= 1:
    try:
        phrase = ' '.join([c for c in sys.stdin.readlines()])
        phrase = str(phrase).strip()
    except:
        print('must take arguments or pipe from stdin')
elif len(sys.argv) > 1:
    param = sys.argv[1]
    phrase = ' '.join(sys.argv[2:])
    phrase = str(phrase).strip()
    # Backup personal dictionary
    if param == '-b':
        shutil.copy(pdict, backup)
        print(pdict + ' was successfully copied to ' + backup)
        sys.exit()
    # Delete entry from personal dictionary
    if param == '-d':
        SAVE = True
        SILENT = True
        DELETE = True
    # No NAEQ - suppress output from NAEQ
    elif param == '-nn':
        SILENT = True
    # No Personal - suppress output from personal dict
    elif param == '-np':
        SAVE = False
        PERSONAL = False
    # Save to personal dictionary
    elif param == '-s':
        SAVE = True
    # Save-Silent to personal dict, suppress NAEQ output
    elif param == '-ss':
        SAVE = True
        SILENT = True
    # Value - query specific numerical value
    elif param == '-v':
        QUERY = True
    # Quiet - suppress all output except for the CEQ value
    elif param == '-q':
        PERSONAL = False
        SILENT = True
    else:
        phrase = ' '.join(sys.argv[1:])
        phrase = str(phrase).strip()

values = []

# Get values from CEB:
if not QUERY:
    for ch in phrase.lower():
        if ch in ceb:
            values.append(ceb[ch])
    value = str(sum(values))
else:
    # For -v parameter, the phrase is querying the value
    try:
        int(phrase)
    except:
        print('The -v parameter only accepts positive integer arguments.')
        print('Please try again with a number.')
        sys.exit()
    value = str(phrase)

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
                    if DELETE:
                        if line != phrase:
                            print(line)
                    else:
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
                if DELETE:
                   new_values.remove(phrase)
                else:
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
