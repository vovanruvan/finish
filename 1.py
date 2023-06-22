import urllib.request
from re import findall
url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"
response = urllib.request.urlopen(url)
data = response.read()
s = data.decode()
phones = findall("\(\d{3}\) \d{3}-\d{4}", s)
for number in phones:
    print(number)