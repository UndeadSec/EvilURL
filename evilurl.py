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
from time import sleep
from os import path
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gaierror

version = python_version().startswith('2', 0, len(python_version()))
if version:
    print('Are you using python version {}\n'
          'Please, use version 3.X of python'.format(python_version()))
    exit(1)

from os import system

RED, WHITE, GREEN, END, YELLOW = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m'

unicodes = {
    'a': '\u0430',
    'A': '\u0410',
    'b': '\u042C',
    'B': '\u0412',
    'c': '\u0441',
    'C': '\u0421',
    'd': '\u0501',
    'D': '',
    'e': '\u0435',
    'E': '\u0415',
    'f': '',
    'F': '',
    'g': '',
    'G': '',
    'h': '\u04BB',
    'H': '\u041D',
    'i': '\u0456',
    'I': '\u0406',
    'j': '\u0458',
    'J': '\u0408',
    'k': '',
    'K': '',
    'l': '',
    'L': '',
    'm': '',
    'M': '\u041C',
    'n': '',
    'N': '',
    'o': '\u043E',
    'O': '\u041E',
    'p': '\u0440',
    'P': '\u0420',
    'q': '\u051B',
    'Q': '\u051A',
    'r': '',
    'R': '',
    's': '\u0455',
    'S': '\u0405',
    't': '',
    'T': '\u0422',
    'u': '',
    'U': '',
    'v': '',
    'V': '',
    'w': '\u051D',
    'W': '\u051C',
    'x': '\u0445',
    'X': '\u0425',
    'y': '\u0443',
    'Y': '\u04AE',
    'z': '',
    'Z': '',
}

def message():
    system('clear')
    print ('''{0}                                                                   
{0}88888888888           88  88{1}  88        88  88888888ba   88           
{0}88                    ""  88{1}  88        88  88      "8b  88           
{0}88                        88{1}  88        88  88      ,8P  88           
{0}88aaaaa  8b       d8  88  88{1}  88        88  88aaaaaa8P'  88           
{0}88"""""  `8b     d8'  88  88{1}  88        88  88""""88'    88      v2.0     
{0}88        `8b   d8'   88  88{1}  88        88  88    `8b    88           
{0}88         `8b,d8'    88  88{1}  Y8a.    .a8P  88     `8b   88           
{0}88888888888  "8"      88  88{1}   `"Y8888Y"'   88      `8b  88888888  {1}
                   	    
			 [ UNDEAD{0}SEC{1} from BR{1}AZIL ]
-> github.com/UndeadSec
-> youtube.com/c/UndeadSec       
                 
How to use:

 Insert name: example
 Insert level domain: .com'''.format(RED, END))


def makeEvil(char, uninum, newurl, end):
    print(
        '\n{2}[*] Char replaced: %s\n[*] Unicode number: %s\n{0}[*] Evil url: %s%s{1}\n-------------------------------'.format(
            GREEN, END, YELLOW) % (char, uninum, newurl, end))


def main():
    message()
    url = input("\n{0}>{1} Insert name: ".format(RED, END))
    end = input("\n{0}>{1} Insert level domain: ".format(RED, END))

    # -------------- FIND CHAR THAT CAN BE REPLACED ----------------- #
    replaced = []
    for i in range(0, len(url)):
        if unicodes[url[i]]:
            replaced.append(i)

    # -------------- Begin REPLACE CHAR ----------------- #
    total = 1 << len(replaced)
    for i in range(1, total):
        urls = list(url)
        rep_char, uni_char = [], []
        for j in range(0, len(replaced)):
            if (i & 1 << j) != 0:
                char = urls[replaced[j]]
                rep_char.append(char)
                uni_char.append(unicodes[char])
                urls[replaced[j]] = unicodes[char]
        makeEvil(','.join(rep_char), ','.join(uni_char), ''.join(urls), end)

    print('\n{0}[*] Total Evil url: %s{1}\n'.format(GREEN, END, YELLOW) % (total - 1))
# -------------- BEGIN CHECKURL MODULE----------------- #
def check_url(url):

    '''
    Check connection
    :param url: suspicious url
    :return: status of connection
    '''

    try:
        url = gethostbyname(url)
    except gaierror as err:
        error = '{1}[*] {0}{2}\n'.format(err,YELLOW,END)
        return error
        exit(1)

    s = socket(AF_INET, SOCK_STREAM)
    check = s.connect_ex((url,80))

    if check == 0:
        msg = '{0}[*] Connection accepted{1}\n'.format(GREEN,END)
    else:
        msg = '{0}[*] Connection refused{1}\n'.format(GREEN, END)

    return msg

def check_EVIL(url):

    '''
    Check evil chars in URL
    :param url: suspicious URL
    :return: result of check and the evil chars
    '''

    result = [url[i] for i in range(len(url)) if url[i] in unicodes.values()]

    if result:
        msg = '\n{0}[*] Evil URL detected: {1}{2}{3}{1}'.format(YELLOW,END,RED,url)
        msg += '\n{0}[*] Evil characters used: {1}{2}{3}{1}'.format(YELLOW,END,RED,result)
    else:
        msg = '\n{0}[*] Evil URL NOT detected:{1} {2}{3}{1}'.format(YELLOW, END, GREEN, url)

    return msg

def urls_list(file):
    '''
    Read the file to verify Evil URL
    :param file: file with a list of Evil URLs
    :return: file reading
    '''

    with open(file) as arq:
        urls = [f.strip() for f in arq]
    for i in range(len(urls)): print(check_EVIL(urls[i]))


def check_list_url(file):

    '''
    Check Evil chars in list of suspicious Evil URL
    :param file: file with a list of Evil URLs
    :return: message with results
    '''

    with open(file) as arq:
        urls_arq = [u.strip() for u in arq]

    msg = ''
    for url in urls_arq:

        bad_chars = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D']
        result = [bad_chars[i] for i in range(len(bad_chars)) if bad_chars[i] in url]
        check_result = check_url(url)

        if result:
            msg += '\n{0}[*] Evil URL detected: {1}{2}{3}{1}'.format(YELLOW, END, RED, url)
            msg += '\n{0}[*] Evil characters used: {1}{2}{3}{1}\n'.format(YELLOW, END, RED, result)
            msg += check_result

        else:
            msg += '\n{0}[*] Evil URL NOT detected:{1} {2}{3}{1}\n'.format(YELLOW, END, GREEN, url)
            msg += check_result

    return msg

def checkURL():
    print ('\n{0}[{1}*{0}]{1} CheckURL module loaded.'.format(GREEN, END))
    print ('\nOperation modes: \n\n{0}[{1}1{0}]{1} Check single URL\n{0}[{1}2{0}]{1} Check from a list'.format(RED, END))
    if input('\n>{0}>{1}> '.format(RED, END)) == '1':
        url = input('{0}>{1} Insert an url: '.format(RED, END))
        print ('\n * Do you want to check connection? (y/n)')
        if input('\n>{0}>{1}> '.format(RED, END)).upper() == 'Y':
            print (check_EVIL(url))
            print (check_url(url))
        else:
            print (check_EVIL(url))
    else:
        fileUrl = input('{0}>{1} Insert file path: '.format(RED, END))
        print ('\n * Do you want to check connections? (y/n)')
        if input('\n>{0}>{1}> '.format(RED, END)).upper() == 'Y':
            print (check_list_url(fileUrl))
        else:
            print (urls_list(fileUrl))

# -------------- END CHECKURL MODULE ----------------- #
def Runner():
    message()
    print ('\nSelect an option: \n\n{0}[{1}1{0}]{1} Generate evil urls\n{0}[{1}2{0}]{1} Detect evil urls'.format(RED, END))
    opt = input('\n>{0}>{1}> '.format(RED, END))
    if opt == '1':
        main()
    elif opt == '2':
        checkURL()
    else:
        print ('{0}[{1}!{0}]{1} Invalid Option.\nReturning to main in few seconds...'.format(RED, END))
        sleep(2)
        Runner()

if __name__ == '__main__':
    try:
        Runner()
    except KeyboardInterrupt:
        exit()
