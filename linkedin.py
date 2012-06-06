import hashlib
import getpass
import re

p = getpass.getpass("Enter your password (it won't be displayed): ")

hex = hashlib.sha1(p).hexdigest()[6:]

passwords = open('combo_not.txt', 'r')

for password in passwords:
  if re.search(hex,password):
    print "The password you typed in was found in the leaked database. You should probably change your LinkedIn password."
    exit()

print "The password you typed was NOT found in the leaked database. You should change your LinkedIn password anyway."
