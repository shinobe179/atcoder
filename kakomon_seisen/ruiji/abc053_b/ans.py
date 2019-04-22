#!/home/shino/.pyenv/shims/python
s = input();print(str(len(s) - s[::-1].index('Z') - s.index('A')))
