while True:
    try:
        x= float(raw_input('Enter the base:'))
        n = float(raw_input('Enter the exponent:'))
    except:
        print 'Invalid input'
        continue
    else:
        break



def power(x, n):
    if n>0:
        return x * power(x, n-1)
    elif n<0:
        return 1/(x * power(x, n-1))
    else:
        return 1
res = power(x,n)
print '{} ^ {} is :{} '.format(x,n,res)
print "Good bye"