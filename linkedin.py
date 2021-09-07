import hashlib
import getpass
import re

p = getpass.getpass("Enter your password (it won't be displayed): ")

hex = hashlib.sha1(p.encode('utf-8')).hexdigest()
hexshort = hex[6:]

passwords = open('combo_not.txt', 'r', encoding='utf-8')

for password in passwords:
  if re.search(hex,password):
    print("The password you typed in was found in the leaked database, but it hasn't yet been cracked in this version of the list. You should probably change your LinkedIn password.")
    exit()
  if re.search(hexshort,password):
    print("The password you typed in was found in the leaked database, and it was already cracked. You should probably change your LinkedIn password.")
    exit()

print("The password you typed was NOT found in the leaked database. Wouldn't hurt to change your LinkedIn password anyway.")
