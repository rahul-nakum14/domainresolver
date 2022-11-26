import requests
import bs4
import time


RED='\033[0;31m'
NC='\033[0m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
LRED = '\033[1;31m'


def test ():
        start = time.perf_counter()
        with open ('domain.txt','r') as f:
            for i in f:
                tmp = site_is_online((i.strip()))
                if tmp:
                        if 'http://' in tmp:
                                domain = "http://"+(i.strip())
                        if 'https://' in tmp:
                                 domain = "https://"+(i.strip())
                        try:
                                                # domain = "https://"+(i.strip())
                                                request_url = requests.get(domain,timeout=2,allow_redirects=True)
                                                domaintext = request_url.text 
                                                soup = bs4.BeautifulSoup(domaintext,'html.parser')
                                                code1 = request_url.status_code
                                                title1 = soup.find("title").text
                                                print(f"{CYAN}{request_url.url}{NC} {RED}{[code1]}{NC} {BLUE}{[title1]}{NC}")
                        except Exception:
                                                print(f"{LRED}{domain} [Something Went Wrong] {NC}")
                # else:
                #        print(f"{LRED}{i.strip()} [Domain is not found] {NC}") 


        finissh = time.perf_counter()
        print(f'Finished in {round(finissh-start ,2)} second (s)')



def site_is_online(url,timeout=2):
        tmp = 'http://'+url
        # tmp1 = 'https://'+url
        try:
                # if requests.head(tmp1,timeout=timeout):
                #         return tmp1
                if requests.head(tmp,timeout=timeout,allow_redirects=True):
                        return tmp
        except Exception :
            print(f"{LRED}{url} [Domain is not found] {NC}")


if __name__ == "__main__":
        test()































# def site_checker(url):
#     connection = HTTPConnection(host=url,timeout=2)
#     try:
#         connection.request('HEAD',"/")
#         return True
#     except Exception:
#         print(f"{LRED}{url} [Domain is not exist]{NC}")
        
        

                

    # avail()
    # t1 = threading.Thread(target=test)
    # t1.start()



