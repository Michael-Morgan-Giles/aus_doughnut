#!/usr/bin/env python
import codecs
import csv

try:
    # Python 3
    from urllib.request import urlopen
except ImportError:
    # Python 2
    from urllib2 import urlopen

# The URL to the collection (as comma-separated values).
collection_url = "https://geoserver-portal.aodn.org.au/geoserver/ows?typeName=imos:anmn_am_dm_data&SERVICE=WFS&outputFormat=csv&REQUEST=GetFeature&VERSION=1.0.0&CQL_FILTER=(site_code%20LIKE%20'NRSMAI')&userId=Guest"

# Fetch data...
response = urlopen(collection_url)

# Iterate on data...
csvfile = csv.reader(codecs.iterdecode(response, 'utf-8'))
for row in csvfile:
    print(row)
