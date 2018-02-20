score = raw_input("Enter Score: ")
try:
    s = float(score)
except:
    print 'Please enter numeric value between 0.0 and 1.0'
    quit()

if 1.0 >= score >= 0.9 :
    print "A"
elif 0.9 > score >= 0.8 :
    print "B"
elif 0.8 > score >= 0.7 :
    print "C"
elif 0.7 > score >= 0.6 :
    print "D"
elif 0.0 <= score  < 0.6 :
    print "F"
else:
    print 'Value is out of range'



