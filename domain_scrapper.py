import requests
import bs4
import time
import sys
import argparse
import os
import threading

RED='\033[0;31m'
NC='\033[0m'
BLUE = '\033[0;94m'
CYAN = '\033[0;96m'
LRED = '\033[1;91m'
Green= '\033[0;92m'  

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input",help="Input domain file")
parser.add_argument("-o","--output",help="Write output to file")
args = parser.parse_args()
outputdata = []

def main():
    start = time.perf_counter()
    try:
        with open(sys.argv[2], 'r') as f:
            threads = []
            for i in f:
                tmp = site_is_online((i.strip()))
                if tmp:
                    domain = "http://" + (i.strip())
                    thread = threading.Thread(target=process_domain, args=(domain,))
                    threads.append(thread)
                    thread.start()
                else:
                        print(f"{LRED}{i.strip()} [Domain is not found] {NC}")
                        outputdata.append(f"{LRED}{i.strip()} [Domain is not found] {NC}")

            for thread in threads:
                thread.join()

        if args.output:
            with open(args.output, 'w') as f:
                for i in outputdata:
                    f.write(i + '\n')

    except Exception as e:
        print("Provide domain file")

    finissh = time.perf_counter()
    print(f'Finished in {round(finissh-start ,2)} second (s)')


def process_domain(domain):
    try:
        request_url = requests.get(domain, timeout=2, allow_redirects=True)
        domaintext = request_url.text
        soup = bs4.BeautifulSoup(domaintext, 'html.parser')
        code1 = request_url.status_code
        title1 = soup.find("title").text
        print(f"{CYAN}{request_url.url}{NC}{RED}{[code1]}{NC} {BLUE}{[title1]}{NC}")
        outputdata.append(f"{CYAN}{request_url.url}{NC}{RED}{[code1]}{NC} {BLUE}{[title1]}{NC}")
    except Exception:
        print(f"{Green}{domain} [Please take a look Manually.] {NC}")


def site_is_online(url,timeout=2):
    try:
        if requests.head('http://'+url,timeout=timeout):
            return 'http://'+url
    except Exception:
        return None


if __name__ == "__main__":
        main()
