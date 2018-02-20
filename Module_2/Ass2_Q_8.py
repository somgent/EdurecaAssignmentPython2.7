L = ['a', 'b', 'c', 'd']
d = {}
for count, elem in enumerate(L):
    d[elem]=(count+1)
print d

"""my_dict = {item : index+1 for index, item in enumerate(L)}
print my_dict"""