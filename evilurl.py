#-*- coding: utf-8 -*-
#------------------------------------------------------
#
#      BY: UNDEADSEC from BRAZIL :)
#      Visit: https://www.youtube.com/c/UndeadSec
#      Github: https://github.com/UndeadSec/EvilURL
#------------------------------------------------------
from os import system
RED, WHITE, GREEN, END, YELLOW = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m'
names = ['Cyrillic Small Letter A', 'Greek Lunate Sigma Symbol', 
'Cyrillic Small Letter Ie', 'Cyrillic Small Letter O', 'Cyrillic Small Letter Er',
'Cyrillic Small Letter Dze', 'Cyrillic Small Letter Komi De', 'Cyrillic Small Letter Qa',
'Cyrillic Small Letter We']

unicodes = ['U+0430', 'U+03F2', 'U+0435', 'U+043E', 'U+0440', 'U+0455', 'U+0501', 'U+051B', 'U+051D']

def message():
    system('clear')
    print '''{0}                                                                   
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
'''.format(RED, END, GREEN, YELLOW)

def makeEvil(char, unicd, uninum, newurl, end):
    print '\n{2}[*] Char replaced: %s\n[*] Using Unicode: %s\n[*] Unicode number: %s\n{0}[*] Evil url: %s%s{1}\n-------------------------------'.format(GREEN, END, YELLOW) % (char, unicd, uninum, newurl, end)

def main():
    message()
    url = raw_input("Insert name: ")
    end = raw_input("Insert level domain: ")
    url = url.lower()
    urlMore = url
    urlChars = ''
    urlNms = ''
    urlUn = ''
    if "A" in url.upper():
        makeEvil('a', names[0], unicodes[0], url.replace('a', u'а'), end)
        urlMore = urlMore.replace('a', u'а')
        urlChars += 'a, '
        urlNms += names[0] + ', '
        urlUn += unicodes[0] + ', '
    if "C" in url.upper():
        makeEvil('c', names[1], unicodes[1], url.replace('c', u'ϲ'), end)
        urlMore = urlMore.replace('c', u'с')
        urlChars += 'c, '
        urlNms += names[1] + ', '
        urlUn += unicodes[1] + ', '
    if "E" in url.upper():
        makeEvil('e', names[2], unicodes[2], url.replace('e', u'е'), end)
        urlMore = urlMore.replace('e', u'e')
        urlChars += 'e, '
        urlNms += names[2] + ', '
        urlUn += unicodes[2] + ', '
    if "O" in url.upper():
        makeEvil('o', names[3], unicodes[3], url.replace('o', u'о'), end)
        urlMore = urlMore.replace('o', u'о')
        urlChars += 'o, '
        urlNms += names[3] + ', '
        urlUn += unicodes[3] + ', '
    if "P" in url.upper():
        makeEvil('p', names[4], unicodes[4], url.replace('p', u'р'), end)
        urlMore = urlMore.replace('p', u'р')
        urlChars += 'p, '
        urlNms += names[4] + ', '
        urlUn += unicodes[4] + ', '
    if "S" in url.upper():
        makeEvil('s', names[5], unicodes[5], url.replace('s', u'ѕ'), end)
        urlMore = urlMore.replace('s', u'ѕ')
        urlChars += 's, '
        urlNms += names[5] + ', '
        urlUn += unicodes[5] + ', '
    if "D" in url.upper():
        makeEvil('d', names[6], unicodes[6], url.replace('d', u'ԁ'), end)
        urlMore = urlMore.replace('d', u'ԁ')
        urlChars += 'd, '
        urlNms += names[6] + ', '
        urlUn += unicodes[6] + ', '
    if "Q" in url.upper():
        makeEvil('q', names[7], unicodes[7], url.replace('q', u'ԛ'), end)
        urlMore = urlMore.replace('q', u'ԛ')
        urlChars += 'q, '
        urlNms += names[7] + ', '
        urlUn += unicodes[7] + ', '
    if "W" in url.upper():
        makeEvil('w', names[8], unicodes[8], url.replace('w', u'ԝ'), end)
        urlMore = urlMore.replace('w', u'ԝ')
        urlChars += 'w.'
        urlNms += names[8] + '.'
        urlUn += unicodes[8] + '.'
    print '\n\n{0}[   MORE EXTENSIVE EVIL URL:   ]{1}'.format(RED, END)
    makeEvil(urlChars, urlNms, urlUn, urlMore, end)
main()
