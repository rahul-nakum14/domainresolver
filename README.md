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
facebook.com
github.com
stackoverflow.com
```

```python script.py -i domain.txt -o output.txt```

output.txt

```
https://www.instagram.com/[200] ['Instagram']
https://github.com/[200] ['GitHub: Let’s build from here · GitHub']
https://stackoverflow.com/[200] ['Stack Overflow - Where Developers Learn, Share, & Build Careers']




```
#Preview

```
https://user-images.githubusercontent.com/106817606/205488375-79b7706a-4bf8-4fcc-a04b-fdce7f1667d5.mp4
```
