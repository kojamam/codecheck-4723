#!/usr/bin/env python3
import sys
from collections import OrderedDict
import urllib.request
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
import json

def urlEncode(url):
    p = urlparse(url)
    query = urllib.parse.quote_plus(p.query, safe='=&')
    url = '{}://{}{}{}{}{}{}{}{}'.format(
        p.scheme, p.netloc, p.path,
        ';' if p.params else '', p.params,
        '?' if p.query else '', query,
        '#' if p.fragment else '', p.fragment)

    return url

def reqAPI(keywords):
    numFounds = OrderedDict()
    baseurl = 'http://54.92.123.84/search?ackey=869388c0968ae503614699f99e09d960f9ad3e12&sort=ReleaseDate asc&rows=1'

    for keyword in keywords:
        query = ''

        query = 'q=Body:' + keyword
        url = baseurl + '&' + query
        req = urllib.request.Request(urlEncode(url))

        with urllib.request.urlopen(req) as response:
            XmlData = response.read()

        root = ET.fromstring(XmlData)
        numFounds[keyword] = int(root[2].attrib['numFound'])

    return numFounds

def main(argv):
    keywords = argv

    numFounds = reqAPI(keywords)

    name = max(numFounds.items(),key=lambda x:x[1])[0]
    count = max(numFounds.values())

    print("{\"name\":\"" + name + "\",\"count\":" + str(count) + "}")
