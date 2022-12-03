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


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("domain.txt",help="input domain file")
parser.add_argument("-o","--output",help="Write output to file")
args = parser.parse_args()

# Use the args.output variable to specify the output file name
with open(args.output, 'w') as output_file:
    output_file.write("xssxsxsx")
