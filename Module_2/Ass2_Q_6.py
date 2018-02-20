'''theDict = {chr(y):y - 64 for y in range(65, 91)}
print theDict'''

x=1
d = {}
for y in range(65,91):
    key = chr(y)
    value = int(x)
    d[key]=value
    x+=1
print d