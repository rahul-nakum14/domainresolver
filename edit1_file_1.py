import threading
import requests
import bs4
import time
import socket
from http.client import HTTPConnection

RED='\033[0;31m'
NC='\033[0m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
LRED = '\033[1;31m'


def test ():
        start = time.perf_counter()
        with open ('domain.txt','r') as f:
            for i in f:
                domain = socket.gethostbyname(i.strip())
                if domain:
                    try:
                            tttt = (i.strip())
                            domain = "https://"+tttt
                            try:
                                dns = socket.gethostbyname(tttt)
                                if dns:
                                    request_url = requests.get(domain,timeout=2,allow_redirects=True)
                                    request_url.url
                                    domaintext = request_url.text 
                                    soup = bs4.BeautifulSoup(domaintext,'html.parser')
                                    code1 = request_url.status_code
                                    title1 = soup.find("title").text
                                    print(f"{CYAN}{domain}{NC} {RED}{[code1]}{NC} {BLUE}{[title1]}{NC}")
                            except Exception:
                                print(f"{LRED}{domain} [Domain is inactive]{NC}")
                            # time.sleep(0.01)

                    except Exception:
                            print("something is wrong")

        finissh = time.perf_counter()
        print(f'Finished in {round(finissh-start ,2)} second (s)')


# def avail():
#     # with open ('domain.txt','r') as f:
#     #         for i in f:
#     #             domain = socket.gethostbyname(i.strip())
#     #             if domain:
#     #                 return domain
#     #                 avail()
#     #             else:
#     #                 print("something went wrong")

#      with open ('domain.txt','r') as f:
#         for i in f:
#             try:
#                 response = requests.get('https://'+i.strip())
#                 return response
#             except:
#                 response= requests.get('http://'+i.strip())
                   

if __name__ == '__main__':
    test()


    # avail()
    # t1 = threading.Thread(target=test)
    # t1.start()



