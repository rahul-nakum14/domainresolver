## Domainresolver

Command line tool to display Status code And title on a list of domains..

## Features
```
usage: script.py [-h] [-i INPUT] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input domain file
  -o OUTPUT, --output OUTPUT
                        Write output to file
```


## Examples

domain.txt 
```
stackoverflow.com
github.com
hackerone.com
not-existdomain.com
instagram.com
youtube.com
404errorpages.com
linkedin.com
bugcrowd.com 
```

```python script.py -i domain.txt -o output.txt```

output.txt

```
https://www.instagram.com/[200] ['Instagram']
https://github.com/[200] ['GitHub: Let’s build from here · GitHub']
https://stackoverflow.com/[200] ['Stack Overflow - Where Developers Learn, Share, & Build Careers']
```
![Screenshot from 2022-12-04 17-21-06](https://user-images.githubusercontent.com/106817606/205488791-4cd933e6-d0da-43fa-b851-7164f76bffed.png)
