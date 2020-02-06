import requests 
import sys 
from termcolor import colored, cprint
cprint("Ebay View Bot by Xystyx, if need any help contact Xystyx#5575 on discord", 'magenta')
cprint('How many views would you like on your ebay listing?', 'blue')
viewsWanted = int(input())
cprint("What is the link of ebay listing you want",'blue')
ebayLink = str(input())
i = 0
while i <= viewsWanted:
    requests.get(ebayLink)
    cprint(i , "blue")
    cprint("Views Completed" ,"green")
    i += 1
cprint("Ebay View by Xystyx completed", 'magenta')