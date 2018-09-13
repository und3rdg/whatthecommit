#! /usr/bin/env python3
# http://whatthecommit.com/
import urllib.request
import re
import argparse
import sys

url = 'http://whatthecommit.com/'
messageRegexp = "content.*<p>(.+?)..</p>"
linkRegexp = 'permalink.*href."/([a-z0-9]*)">permalink'

def html():
    request = urllib.request.Request(url)
    try:
        opener = urllib.request.urlopen(request, timeout=10)
    except urllib.error.URLError as e:
        print(e.reason)
    html = opener.read()
    return html

def flags(): # CLI ARGUMENTS
    message = re.findall(messageRegexp, str(html()))[0]
    message = '\n' + message
    link = re.findall(linkRegexp, str(html()))[0]
    link = url + link

    parser = argparse.ArgumentParser()
    
    # FLAGS
    parser.add_argument('-o', '--only', help='show only message', action='store_true')

    args = parser.parse_args()
    # LOCAL IP
    if args.only:
        print(message)
    else:
        print(message)
        print(link)
flags()
