import sys

print "YOU HAVE BEEN PWNED!"

import urllib2
print urllib2.urlopen("https://api.ipify.org/?format=json").read()

#while True:
#    continue

sys.exit(0);

