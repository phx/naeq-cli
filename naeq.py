#!/usr/bin/env python3

import sys, liber_al

naeq = liber_al.vel_legis()

ceb = {
      "a": 1,"b": 20,"c": 13,"d": 6,"e": 25,"f": 18,"g": 11,"h": 4,"i": 23,"j": 16,"k": 9,
      "l": 2,"m": 21,"n": 14,"o": 7,"p": 26,"q": 19,"r": 12,"s": 5,"t": 24,"u": 17,"v": 10,
      "w": 3,"x": 22,"y": 15,"z": 8
      }

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
    phrase = ' '.join(sys.argv[1:])
    phrase = phrase.strip()
    try:
        phrase = int(phrase)
    except:
        pass

values = []

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

print('---------------------------------------------------------------')
print('PHRASE: ' + str(phrase))
print('AEQ VALUE: ' + value)
print('---------------------------------------------------------------')
print('NAEQ MATCHES:')
print('---------------------------------------------------------------')
if value in naeq.keys():
    for line in naeq[value]:
        print(line)
