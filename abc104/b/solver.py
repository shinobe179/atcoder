#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

s = input()
C_count = 0

if s[0] == 'A' and s[2:-1].count('C') == 1:
    for i in range(1, len(s)):
        if s[i].isupper():
            if s[i] == 'C':
                C_count += 1
            else:
                print('WA')
                sys.exit()

if C_count != 1:
    print('WA')
    sys.exit()
else:
    print('AC')
