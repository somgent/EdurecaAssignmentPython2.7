dict1= {'a':1,'b':2}
print dict1.items()
rev_Dict = {}
for k, v in dict1.iteritems():
    rev_Dict[v] = rev_Dict.get(v, [])
    rev_Dict[v].append(k)
print rev_Dict

dict1 = { 'a': 1, 'b':2 }
dict2 = {value:key for key, value in dict1.items()}
print(dict2)