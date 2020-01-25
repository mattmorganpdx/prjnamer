#!/usr/bin/env python
try:
    from bs4 import BeautifulSoup
    import requests
    import random
except ImportError as ie:
    print("please 'pip install {}'".format(str(ie).split()[3]))
    exit(1)

# We are going to pick a famous comedian with a unique last name.
soup = None
local = False
if local is True:
    # local file for dev so you don't have to wait for the request.
    url = "local_index.html"
    soup = BeautifulSoup(open(url), 'html.parser')
else:
    url = "https://en.wikipedia.org/wiki/List_of_comedians"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

# looking at the html all the names we want are wrapped in <li> blocks
lis = soup.find_all('li')

# Use a dict so we condense common lasts names into just one choice. A cheap way to get a set.
names = {}
# We'll convert that dict to a list because it's easier to work with.
name_list = []

for l in lis:
    # only get fields that are two words.
    if l.string and len(l.string.split()) is 2:
        x = l.string.split()
        names[x[1]] = x[0]

for n in names.keys():
    name_list.append(names[n] + " " + n)

choice = random.choice(name_list)

print("How about calling your git project {} or {}".format(choice.split()[1].lower(), choice.replace(" ", "").lower()))






