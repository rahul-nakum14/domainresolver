import requests
import bs4

domain = "https://"+input()
request_url = requests.get(domain)
domaintext = request_url.text 

soup = bs4.BeautifulSoup(domaintext,'html.parser')
print(request_url.status_code)
print(soup.find("title").text)


'''

method 1 --

soup = bs4.BeautifulSoup(domaintext, 'html.parser')
print(soup.find('title').text)

method 2 --
titleprint = domaintext[domaintext.find('<title>') + 7 : domaintext.find('</title>')]

method 3-- 

titleprint = re.search('(?im)<\s*title.*>(.*?)<\s*/\s*title>',domaintext)
print(titleprint.groups())

'''



