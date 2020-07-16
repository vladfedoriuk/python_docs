a = dict(A=-1, Z=1)
print(a)

b = {'A': -1, 'Z': 1}
print(b)

c = dict(zip(['A', 'Z'], [-1, 1]))
print(c)

d = dict([('A', -1), ('Z', 1)])
print(d)

e = dict({'A': -1, 'Z': 1})
print(a == b == c == d == e)

# is = whether objects have the same id, not only the value
print(list(zip(['h', 'e', 'l', 'l', 'o'], range(5))))
f = dict(list(zip(['h', 'e', 'l', 'l', 'o'], range(5))))
print(f)
print(d.keys())
print(d.values())
print(d.items())

print(f.popitem())
print(f.pop('l'))
try:
    f.pop('l')
except KeyError:
    print("already deleted")

f.update({'another': 'value'})
f.update(a=1)
print(f)
d.get('a')  # the same as d['a'] but if the key is missing, no KeyError
d.get('a', 177)  # default value is returned if the key is missing
print(d.get('b', 177))  # like this

g = {}
v = g.setdefault('a', 1)  # it behaves like get() but also sets the key with a given value if it is not there
print(v)
print(g)
g.setdefault('a', 2)
print(g)
g['a'] = 3
print(g)
g.pop('a')
print(g)
print(g.get('a'))

x = {}
x.setdefault('a', {}).setdefault('b', []).append(1)
print(x)