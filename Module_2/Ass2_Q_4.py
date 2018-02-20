hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print "Enter a numeric value: "
    quit()
gross = h*r
print "Gross pay is ", '%0.2f' % gross
