import os

a = open("first.txt").read().split()
b = open("last.txt").read().split()
a = a[:len(b)]
print len(a), len(b)

#username = raw_input("Enter Gmail Username: ")

usernames = []; valids = []
for i in range(0, len(a)):
    usernames.append("%s.%s" % (a[i], b[i]))

for username in usernames:
    print "Checking If %s@gmail.com Exists..." % username
    os.system("curl -v https://mail.google.com/mail/gxlu?email=%s@gmail.com 2> email.txt" % username)
    x = open("email.txt").read()
    if "set-cookie:" in " ".join(x.split()):
        print "lulz, it works... user %s.%s@gmail.com exists!" % (a[i], b[i])
        valids.append("%s.%s@gmail.com" % (a[i], b[i]))
    else:
        print "user doesn't exist"

print "\nScan Complete!\n"
for valid in valids:
    print valid
