# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# Import regular expressions
import re 

import urllib

import sys

import email

#-----------------------------------------------------------

#get all the relevant links
commander_link = raw_input('Enter the EDHRec commander page link: ')

#scrape the pages
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
commander_response = requests.get(commander_link, headers=headers)

#parse the HTML
commander_soup = BeautifulSoup(commander_response.text, "html.parser")

#create lists of soup contents
commander = commander_soup.findAll("div", { "class" : "nwname"})

print commander[2]
