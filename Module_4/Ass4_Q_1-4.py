

# write a regular expression that will match a date as follows the following standard :YYYY=DD-MM"

from datetime import date
from re import compile


#+==================DATE==================
test_str = """
            rfdFAJN g 2018-12-28sdfSDG
            vn av  awljen  f1982-10-10 fsdf
            asdsds 2004-11-20FJAF SAEKJF Nsakfj
           """
pattern1 = compile("\d{4}-\d{2}-\d{2}")
today = date.today().strftime("%Y-%m-%d")

print(pattern1.findall(test_str))

if pattern1.search(today):
    print "Today's date is in 'YYYY-MM-DD' format: %s" % today
print '\n\n'

#===================traditional SSN====================

pattern2 = compile("^\d{3}-\d{2}-\d{4}$")

ssn_list = ["234-56-5924", "12-5-78912", "123-5-7891", "1123-56-7777", "006-07-0001"]

for ssn in ssn_list:
    if pattern2.match(ssn):
        print "%s is a valid SSN." % ssn
    else:
        print "%s is an invalid SSN." % ssn
print '\n\n'

#===================IPv4 Match====================

pattern = compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
# ^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$
ip_list = ["192.168.0.1", "1023.123.44.1", "999.999.999.999", "10.8.0.40", "0.0.0.0", "255.255.255.0"]

for ip in ip_list:
    if pattern.match(ip):
        print "%s is a valid IPv4 IP." % ip
    else:
        print "%s is an invalid IPv4 IP." % ip

print '\n\n'

#===================Email Match====================

pattern = compile("[\w._\-]+@\w+\.[a-zA-Z.]{3}")
email_list = ["soumen.ugent@gmail.com",
              "sam_2005@rediffmail.com",
              "abhaya.233@yahoo.co.in",
              "rebeca@gmail.net",
              "djhe c z v@0.0",
              "123.yrftdd@3032.com",
              "edureka.co"
              ]

for email in email_list:
    if pattern.match(email):
        print "%s is a valid email id." % email
    else:
        print "%s is an invalid email id." % email