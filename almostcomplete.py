import requests
import bs4
import time
import sys
import argparse
import os

RED='\033[0;31m'
NC='\033[0m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
LRED = '\033[1;31m'

parser = argparse.ArgumentParser()
parser.add_argument("domain.txt",help="input domain file")
parser.add_argument("-o","--Output",help="Write output to file")
args = parser.parse_args()

def test ():
        start = time.perf_counter()
        try:
                with open (sys.argv[1],'r') as f:
                        for i in f:
                                tmp = site_is_online((i.strip()))
                                if tmp:
                                        # if 'http://' in tmp:
                                        domain = "http://"+(i.strip())
                                        # if 'https://' in tmp:
                                        #          domain = "https://"+(i.strip())
                                        try:
                                                                # domain = "https://"+(i.strip())
                                                                request_url = requests.get(domain,timeout=2,allow_redirects=True)
                                                                domaintext = request_url.text 
                                                                soup = bs4.BeautifulSoup(domaintext,'html.parser')
                                                                code1 = request_url.status_code
                                                                title1 = soup.find("title").text
                                                                if args.Output:
                                                                        fd = os.open(sys.argv[3],os.O_RDWR|os.O_CREAT)
                                                                        s = title1
                                                                        line = str.encode(s)
                                                                        os.write(fd,line)
                                                                        os.linesep
                                                                        # os.write(fd,(f"{CYAN}{request_url.url}{NC}{RED}{[code1]}{NC} {BLUE}{[title1]}{NC}").encode())
                                                                        os.close(fd)
                                                                print(f"{CYAN}{request_url.url}{NC}{RED}{[code1]}{NC} {BLUE}{[title1]}{NC}")
                                        except Exception:
                                                                print(f"{LRED}{domain} [Something Went Wrong] {NC}")

                                else:
                                        print(f"{LRED}{i.strip()} [Domain is not found] {NC}")
                finissh = time.perf_counter()
                print(f'Finished in {round(finissh-start ,2)} second (s)')
        except Exception as e:
                print("Provide domain file")


def site_is_online(url,timeout=2):
        tmp = 'http://'+url
        try:

                if requests.head('http://'+url,timeout=timeout):
                        return tmp
        except Exception :
                return
        #     print(f"{LRED}{url} [Domain is not found] {NC}")
            


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



