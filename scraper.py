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
deck_url = raw_input('Enter the Deckbox text export link: ')
commander_link = raw_input('Enter the EDHRec commander page link: ')
inventory_link = raw_input('Enter your Deckbox collection link: ')

#scrape the pages
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
deck_response = requests.get(deck_url, headers=headers)
inventory_response = requests.get(inventory_link, headers=headers)
commander_response = requests.get(commander_link, headers=headers)

#parse the HTML
deck_soup = BeautifulSoup(deck_response.text, "html.parser")
inventory_soup = BeautifulSoup(inventory_response.text, "html.parser")
commander_soup = BeautifulSoup(commander_response.text, "html.parser")

#create lists of soup contents
deck = deck_soup.body.contents
inventory = inventory_soup.body.contents
commander = commander_soup.findAll("div", { "class" : "nwname"})

#fix up the lists so we can compare
del deck[1::2]
del inventory[1::2]

print(deck.get_text())
print("-----")
print(commander.get_text())
