def test():
    start = time.perf_counter()
    try:
        with open(sys.argv[1], 'r') as f:
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
                        output_line = f"{CYAN}{request_url.url}{NC}{RED}{[code1]}{NC} {BLUE}{[title1]}{NC}"
                        if args.output:
                            with open(args.output, 'w') as f:
                                f.write(output_line + '\n')
                        else:
                            print(output_line)
                    except Exception:
                        print(f"{LRED}{domain} [Something Went Wrong] {NC}")
                else:
                    print(f"{LRED}{i.strip()} [Domain is not found] {NC}")
        finissh = time.perf_counter()
        print(f'Finished in {round(finissh-start ,2)} second (s)')
    except Exception as e:
        print("Provide domain file")


# import sys
# import argparse
# import requests

# parser = argparse.ArgumentParser()
# parser.add_argument("input_file", help="the input file to read from")
# parser.add_argument("-o", "--output", help="the output file to write to")
# args = parser.parse_args()

# with open (sys.argv[1],'r') as f:
#     for i in f:
#         if requests.get(i.strip()):
#             print(i.strip())
#         else:
#             print("not")

#         if args.output:
#                         with open(sys.argv[3], 'w') as Output:
#                             Output.writelines(i.strip())


# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("domain.txt",help="input domain file")
# parser.add_argument("-o","--output",help="Write output to file")
# args = parser.parse_args()

# # Use the args.output variable to specify the output file name
# with open(args.output, 'w') as output_file:
#     output_file.write("xssxsxsx")
