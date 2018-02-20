temperature = raw_input("Enter a temperature in Fahrenheit: ")
try:
    F = float(temperature)
except:
    print "Please enter a valid temperature "
    quit()
C = 5*((F-32)/9.)
print "Equivalent temperature in Celsius is", '%0.2f' %C



