from itertools import product

m = {'a':['a','4','@'],'e':['e','3'],'i':['i','1','!'],'l':['l','1'],
     'o':['o','0'],'t':['t','7'],'s':['s','5','$'],'b':['b','8'],'z':['z','2']}

out = set()
with open('wordlist.txt') as f:
    for w in f:
        w = w.strip()
        out.update(''.join(p) for p in product(*[m.get(c.lower(), [c]) for c in w]))

with open('l33t_guesses.txt', 'w') as fo:
    fo.writelines(s + '\n' for s in sorted(out))