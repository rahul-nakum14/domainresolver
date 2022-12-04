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
parser.add_argument("-i","--input",help="input domain file")
parser.add_argument("-o","--output",help="Write output to file")
args = parser.parse_args()
outputdata = []

def main():
    start = time.perf_counter()
    try:
        with open(sys.argv[2], 'r') as f:
            for i in f:
                tmp = site_is_online((i.strip()))
                if tmp:
                    domain = "http://" + (i.strip())
                    try:
                        request_url = requests.get(
                            domain, timeout=2, allow_redirects=True)
                        domaintext = request_url.text
                        soup = bs4.BeautifulSoup(domaintext, 'html.parser')
                        code1 = request_url.status_code
                        title1 = soup.find("title").text
                        print(f"{CYAN}{request_url.url}{NC}{RED}{[code1]}{NC} {BLUE}{[title1]}{NC}")
                        outputdata.append(f"{CYAN}{request_url.url}{NC}{RED}{[code1]}{NC} {BLUE}{[title1]}{NC}")
                        
                    except Exception:
                        print(f"{LRED}{domain} [Something Went Wrong] {NC}")
                else:
                        print(f"{LRED}{i.strip()} [Domain is not found] {NC}")
                        outputdata.append(f"{LRED}{i.strip()} [Domain is not found] {NC}")

        if args.output:
                                with open(args.output, 'w') as f:
                                        for i in outputdata:
                                                f.write(i + '\n')


    except Exception as e:
        print("Provide domain file")

        finissh = time.perf_counter()
        print(f'Finished in {round(finissh-start ,2)} second (s)')


def site_is_online(url,timeout=2):
    try:
        if requests.head('http://'+url,timeout=timeout):
            return 'http://'+url
    except Exception:
        return None


if __name__ == "__main__":
        main()
