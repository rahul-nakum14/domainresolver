import threading
import requests
import bs4
import time

start = time.perf_counter()
def test ():
    with open ('c:\\Users\\rahul\\Desktop\\Python\\codechef\\Python Project\\domain.txt','r') as f:

    
        start = time.perf_counter()
        for i in f:
            tttt = (i.strip())
            domain = "https://"+tttt
        
            request_url = requests.get(domain)
            domaintext = request_url.text 

            soup = bs4.BeautifulSoup(domaintext,'html.parser')
            print(request_url.status_code)
            print(soup.find("title").text)
            time.sleep(0.01)

        finissh = time.perf_counter()
        print(f'Finished in {round(finissh-start ,2)} second (s)')

if __name__ == '__main__':
    t1 = threading.Thread(target=test)
    t1.start()


    
# print(start - 2789200.5593500,2)

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



