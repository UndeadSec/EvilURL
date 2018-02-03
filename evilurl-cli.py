#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Original version by UNDEADSEC - https://github.com/UndeadSec/EvilURL
#   hackOx version by @deantonious

import argparse, sys, socket
from time import sleep
from os import path
from os import system

def banner():
    print('''
  _____       _ _ _   _ ____  _           ____ _     ___ 
 | ____|_   _(_) | | | |  _ \| |         / ___| |   |_ _|
 |  _| \ \ / / | | | | | |_) | |   _____| |   | |    | |    
 | |___ \ V /| | | |_| |  _ <| |__|_____| |___| |___ | | 
 |_____| \_/ |_|_|\___/|_| \_\_____|     \____|_____|___|  v1.0                                                       
''')
names = ["Cyrillic Small Letter A",
         "Greek Lunate Sigma Symbol",
         "Cyrillic Small Letter Ie",
         "Cyrillic Small Letter O",
         "Cyrillic Small Letter Er",
         "Cyrillic Small Letter Dze",
         "Cyrillic Small Letter Komi De",
         "Cyrillic Small Letter Qa",
         "Cyrillic Small Letter We"]

unicodes = ["\u0430", "\u03F2", "\u0435", "\u043E", "\u0440", "\u0455", "\u0501", "\u051B", "\u051D"]

def makeEvil(char, unicd, uninum, newurl, end, checkConnection):
    print("[*] Char replaced: {}\n[*] Using Unicode: {}\n[*] Unicode number: {}\n[*] Evil url: {}.{}".format(char, unicd, uninum, newurl, end))
    if checkConnection == True:
        print(checkURL("{}.{}".format(newurl, end)))
    print("-------------------------------")

def generate(fullUrl, checkConnection):
    print("\n[   GENERATED EVIL URLS:   ]")
    url = fullUrl.split(".")[0].lower()
    end = fullUrl.split(".")[1].lower()
    urlMore = url
    urlChars = ""
    urlNms = ""
    urlUn = ""

    if "a" in url:
        makeEvil("a", names[0], unicodes[0], url.replace("a", "\u0430"), end, checkConnection)
        urlMore = urlMore.replace("a", "\u0430")
        urlChars += "a, "
        urlNms += names[0] + ", "
        urlUn += unicodes[0] + ", "

    if "c" in url:
        makeEvil("c", names[1], unicodes[1], url.replace("c", "\u03F2"), end, checkConnection)
        urlMore = urlMore.replace("c","\u03F2")
        urlChars += "c, "
        urlNms += names[1] + ", "
        urlUn += unicodes[1] + ", "

    if "c" in url:
        makeEvil("e", names[2], unicodes[2], url.replace("e", "\u0435"), end, checkConnection)
        urlMore = urlMore.replace("e", "\u0435")
        urlChars += "e, "
        urlNms += names[2] + ", "
        urlUn += unicodes[2] + ", "

    if "o" in url:
        makeEvil("o", names[3], unicodes[3], url.replace("o", "\u043E"), end, checkConnection)
        urlMore = urlMore.replace("o", "\u043E")
        urlChars += "o, "
        urlNms += names[3] + ", "
        urlUn += unicodes[3] + ", "

    if "p" in url:
        makeEvil("p", names[4], unicodes[4], url.replace("p", "\u0440"), end, checkConnection)
        urlMore = urlMore.replace("p", "\u0440")
        urlChars += "p, "
        urlNms += names[4] + ", "
        urlUn += unicodes[4] + ", "

    if "s" in url:
        makeEvil("s", names[5], unicodes[5], url.replace("s", "\u0455"), end, checkConnection)
        urlMore = urlMore.replace("s", "\u0455")
        urlChars += "s, "
        urlNms += names[5] + ", "
        urlUn += unicodes[5] + ", "

    if "d" in url:
        makeEvil("d", names[6], unicodes[6], url.replace("d", "\u0501"), end, checkConnection)
        urlMore = urlMore.replace("d", "\u0501")
        urlChars += "d, "
        urlNms += names[6] + ", "
        urlUn += unicodes[6] + ", "

    if "q" in url:
        makeEvil("q", names[7], unicodes[7], url.replace("q", "\u051B"), end, checkConnection)
        urlMore = urlMore.replace("q","\u051B")
        urlChars += "q, "
        urlNms += names[7] + ", "
        urlUn += unicodes[7] + ", "

    if "w" in url:
        makeEvil("w", names[8], unicodes[8], url.replace("w","\u051D"), end, checkConnection)
        urlMore = urlMore.replace("w", "\u051D")
        urlChars += "w."
        urlNms += names[8] + "."
        urlUn += unicodes[8] + "."

    print ("\n[   MORE EXTENSIVE EVIL URL:   ]")
    makeEvil(urlChars, urlNms, urlUn, urlMore, end, checkConnection)

def checkURL(url):
    try:
        socket.gethostbyname(url)
        msg = "[*] Connection accepted"
    except socket.error:
        msg = "[*] Connection refused"
    return msg

def checkEvil(url):
    bad_chars = ["\u0430", "\u03F2", "\u0435", "\u043E", "\u0440", "\u0455", "\u0501", "\u051B", "\u051D"]
    result = [bad_chars[i] for i in range(len(bad_chars)) if bad_chars[i] in url]

    if result:
        msg = "[*] Evil URL detected: {}".format(url)
        msg += "\n[*] Evil characters used: {}".format(result)
    else:
        msg = "[*] Evil URL NOT detected: {}".format(url)
    return msg

if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(usage="evilurl-cli.py {domain} [options]", description="Command line version of EvilURL")
    parser.add_argument("domain", help="Domain name with termination (example.com)")
    parser.add_argument("-cE", dest="check", action="store_true", help="Check if url is evil (won't generate evil url)")
    parser.add_argument("-cC", dest="checkConnection", action="store_true", help="Check generated/input domain connections")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    domain = args.domain
    check = args.check
    checkConnection = args.checkConnection

    if domain == None:
        print("Invalid options. Use -h or --help to view available options.")
        exit()
    if check == True:
        print(checkEvil(domain))
        if checkConnection == True:
            print(checkURL(domain))
    else:
        generate(domain, checkConnection)
