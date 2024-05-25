import collections
from collections import defaultdict
from collections import ChainMap

#Ordered dict
d = collections.OrderedDict(one=1, two=2, three=3)

print(d)

d["four"] = 4

print(d)

print(d.keys())


# Default dict
dd = defaultdict(list)

dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr. Sniffles')

print(dd['dogs'])

# Chain map
dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
chain = ChainMap(dict1, dict2)

print(chain)
print(chain['one'])
print(chain['three'])