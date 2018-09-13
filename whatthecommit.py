#! /usr/bin/env python3
# http://whatthecommit.com/
import urllib.request
import re
import argparse
url = 'http://whatthecommit.com/'

def getCommit():
    request = urllib.request.Request(url)
    try:
        opener = urllib.request.urlopen(request, timeout=10)
    except urllib.error.URLError as e:
        print(e.reason)
    html = opener.read()

    regexp = {
        'msg': 'content.*<p>(.+?)..</p>',
        'link': 'permalink.*href."/([a-z0-9]*)">permalink'
    }
    grep = {
        'commit' : re.findall(regexp['msg'], str(html))[0],
        'link' : url + re.findall(regexp['link'], str(html))[0]
    }

    args = flags()
    out = grep['commit'].replace('\\', '')
    if args.verbose:
        out = ( out + '\n' 
                + grep['link'])
    return out


def flags(): # CLI ARGUMENTS
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='Include refLink to commit message.', action='store_true')
    args = parser.parse_args()
    return args

print(getCommit())

