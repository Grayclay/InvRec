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

import urllib.request

import sys

import email

#-----------------------------------------------------------

#get all the relevant links
deck_url = input('Enter the Deckbox text export link: ')
commander_link = input('Enter the EDHRec commander page link: ')
inventory_link = input('Enter your Deckbox collection link: ')

#scrape the pages
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
deck_response = requests.get(deck_url, headers=headers)
inventory_response = requests.get(inventory_link, headers=headers)


#parse the HTML
deck_soup = BeautifulSoup(deck_response.text, "html.parser")
inventory_soup = BeautifulSoup(inventory_response.text, "html.parser")

#create an empty list
deck = deck_soup.body.contents

#delete the br/ tags from teh soup
del deck[1::2]

#iterate through the parsed HTML and extract dates
print (*deck, sep='\n')