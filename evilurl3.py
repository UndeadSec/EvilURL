#-*- coding: utf-8 -*-
#------------------------------------------------------
#
#      BY: UNDEADSEC from BRAZIL :)
#      Visit: https://www.youtube.com/c/UndeadSec
#      Github: https://github.com/UndeadSec/EvilURL
#------------------------------------------------------

from __future__ import print_function
from platform import python_version
from sys import exit

version = python_version().startswith('2', 0, len(python_version()))
if version:
    print('Are you using python version {}\n'
          'Please, use version 3.X of python'.format(python_version()))
    exit(1)

from os import system

RED, WHITE, GREEN, END, YELLOW = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m'

names = ['Cyrillic Small Letter A',
         'Greek Lunate Sigma Symbol',
         'Cyrillic Small Letter Ie',
         'Cyrillic Small Letter O',
         'Cyrillic Small Letter Er',
         'Cyrillic Small Letter Dze',
         'Cyrillic Small Letter Komi De',
         'Cyrillic Small Letter Qa',
         'Cyrillic Small Letter We']

unicodes = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D']

def message():
    system('clear')
    print ('''{0}                                                                   
{0}88888888888           88  88{1}  88        88  88888888ba   88           
{0}88                    ""  88{1}  88        88  88      "8b  88           
{0}88                        88{1}  88        88  88      ,8P  88           
{0}88aaaaa  8b       d8  88  88{1}  88        88  88aaaaaa8P'  88           
{0}88"""""  `8b     d8'  88  88{1}  88        88  88""""88'    88           
{0}88        `8b   d8'   88  88{1}  88        88  88    `8b    88           
{0}88         `8b,d8'    88  88{1}  Y8a.    .a8P  88     `8b   88           
{0}88888888888  "8"      88  88{1}   `"Y8888Y"'   88      `8b  88888888888  {1}
                   	    
			 [ UNDEAD{0}SEC{1} from {2}B{3}R{1}AZIL ]
-> github.com/UndeadSec
-> youtube.com/c/UndeadSec       
                 
How to use:

 Insert name: example
 Insert level domain: .com                                                                
'''.format(RED, END, GREEN, YELLOW))

def makeEvil(char, unicd, uninum, newurl, end):
    print('\n{2}[*] Char replaced: %s\n[*] Using Unicode: %s\n[*] Unicode number: %s\n{0}[*] Evil url: %s%s{1}\n-------------------------------'.format(GREEN, END, YELLOW) % (char, unicd, uninum, newurl, end))

def main():
    message()
    url = input("Insert name: ")
    end = input("Insert level domain: ")
    url = url.lower()
    urlMore = url
    urlChars = ''
    urlNms = ''
    urlUn = ''

    if "A" in url.upper():
        makeEvil('a', names[0], unicodes[0], url.replace('a', '\u0430'), end)
        urlMore = urlMore.replace('a', '\u0430')
        urlChars += 'a, '
        urlNms += names[0] + ', '
        urlUn += unicodes[0] + ', '

    if "C" in url.upper():
        makeEvil('c', names[1], unicodes[1], url.replace('c', '\u03F2'), end)
        urlMore = urlMore.replace('c','\u03F2')
        urlChars += 'c, '
        urlNms += names[1] + ', '
        urlUn += unicodes[1] + ', '

    if "E" in url.upper():
        makeEvil('e', names[2], unicodes[2], url.replace('e', '\u0435'), end)
        urlMore = urlMore.replace('e', '\u0435')
        urlChars += 'e, '
        urlNms += names[2] + ', '
        urlUn += unicodes[2] + ', '

    if "O" in url.upper():
        makeEvil('o', names[3], unicodes[3], url.replace('o', '\u043E'), end)
        urlMore = urlMore.replace('o', '\u043E')
        urlChars += 'o, '
        urlNms += names[3] + ', '
        urlUn += unicodes[3] + ', '

    if "P" in url.upper():
        makeEvil('p', names[4], unicodes[4], url.replace('p', '\u0440'), end)
        urlMore = urlMore.replace('p', '\u0440')
        urlChars += 'p, '
        urlNms += names[4] + ', '
        urlUn += unicodes[4] + ', '
 
    if "S" in url.upper():
        makeEvil('s', names[5], unicodes[5], url.replace('s', '\u0455'), end)
        urlMore = urlMore.replace('s', '\u0455')
        urlChars += 's, '
        urlNms += names[5] + ', '
        urlUn += unicodes[5] + ', '

    if "D" in url.upper():
        makeEvil('d', names[6], unicodes[6], url.replace('d', '\u0501'), end)
        urlMore = urlMore.replace('d', '\u0501')
        urlChars += 'd, '
        urlNms += names[6] + ', '
        urlUn += unicodes[6] + ', '

    if "Q" in url.upper():
        makeEvil('q', names[7], unicodes[7], url.replace('q', '\u051B'), end)
        urlMore = urlMore.replace('q','\u051B')
        urlChars += 'q, '
        urlNms += names[7] + ', '
        urlUn += unicodes[7] + ', '
 
    if "W" in url.upper():
        makeEvil('w', names[8], unicodes[8], url.replace('w','\u051D'), end)
        urlMore = urlMore.replace('w', '\u051D')
        urlChars += 'w.'
        urlNms += names[8] + '.'
        urlUn += unicodes[8] + '.'

    print ('\n\n{0}[   MORE EXTENSIVE EVIL URL:   ]{1}'.format(RED, END))
    makeEvil(urlChars, urlNms, urlUn, urlMore, end)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()