from operator import itemgetter
Mylist = [['John',1,'a'],['Larry',0,'b']]
print sorted(Mylist,key = itemgetter(1))