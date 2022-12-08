## DomainScrapper

This is a simple python script to scrape domain information such as HTTP status code and title. It takes a list of domains as input and display the information in the terminal as well as write in a specified output file.


## Installation

```pip install -r requirements.txt```

## Usage
```
python domain_scrapper.py -i <input_file> -o <output_file>
```
## Arguments

 +   `-i` or `--input`: Input file containing the list of domains
 +   `-o` or `--output`: Output file to write the domain information (optional)


## Example
```
python domain_scrapper.py -i domain_list.txt -o domain_info.txt
```

domain.txt 
```
google.com
test.com
```

## Output
The output will be in the following format:
```
<domain_url> <http_status_code> <title>
```
For example:
```
http://google.com [200] [Google]
http://test.com [404] [Page Not Found]
```
