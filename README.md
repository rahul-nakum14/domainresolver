## DomainScrapper

This is a simple python script to scrape domain information such as HTTP status code and title. It takes a list of domains as input and outputs the information in the terminal as well as in a specified output file.


## Installation

```pip install -r requirement.txt```

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


## Example
![Screenshot from 2022-12-04 17-21-06](https://user-images.githubusercontent.com/106817606/205488791-4cd933e6-d0da-43fa-b851-7164f76bffed.png)
