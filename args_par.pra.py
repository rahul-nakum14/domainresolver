import argparse


parser = argparse.ArgumentParser()
parser.add_argument("num1",metavar="Enter num 1",type=int)
parser.add_argument("--num2",metavar="Enter num 2",type=int)
# parser.add_argument("--operation",help="Enter Opearation",choices=["add","sub","div"])
# parser.add_argument("This from opt.",metavar='Helo from option args.....')
parser.add_argument('--foo', metavar='YYY')
args = parser.parse_args()

if args.operation == "add":
    print("Result is",args.num1+args.num2)
elif args.operation == "sub":
    print("Result is",args.num1-args.num2)
elif args.operation == "div":
    print("Result is",args.num1/args.num2)
else:
    print("unsupported xd")

#     import argparse
# import os

# parser = argparse.ArgumentParser()
# parser.add_argument("num1",help="Enter num input file")
# parser.add_argument("-o","--output",help="Write output to file")
# # parser.add_argument("--operation",help="Enter Opearation")
# # parser.add_argument("This from opt.",metavar='Helo from option args.....')
# # parser.add_argument('--foo', metavar='YYY')
# args = parser.parse_args()

# if args.operation == "add":
#     print("Result is",args.num1+args.num2)
# elif args.operation == "sub":
#     print("Result is",args.num1-args.num2)
# elif args.operation == "div":
#     print("Result is",args.num1/args.num2)
# else:
#     print("unsupported xd")



























# parser = argparse.ArgumentParser()
# parser.add_argument('--output', type=argparse.FileType('w'),default='-')
# parser.add_argument("--o to out file")
# parser.add_argument(
#         "-o",
#         "--output",
#         help='The file to save the Links output to, including path if necessary (default: output.txt). If set to "cli" then output is only written to STDOUT. If the file already exist it will just be appended to (and de-duplicated) unless option -ow is passed.',
#     )

# args = parser.parse_args()


# args = parser.parse_args()
# with open (sys.argv[1],'r') as f:
#     f.write('lllllllllll.txt')

# with open(args.output, 'w') as output_file:
#     output_file.write("%s\n" % item)
