#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen

def scrape():
    url = 'https://chaturbate.com/animergamergirl'
    response = urlopen(url)
    html = response.read()
    if html.find('Room is currently offline') != -1:
     return False
    return True

