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
deck_url = input('Enter the Deckbox text export link: ')
commander_link = input('Enter the EDHRec commander page link: ')
inventory_link = input('Enter your Deckbox collection link: ')


#scrape the pages
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
deck_response = requests.get(deck_url, headers=headers)
inventory_response = requests.get(inventory_link, headers=headers)
commander_response = requests.get(commander_link, headers=headers)


#parse the HTML
deck_soup = BeautifulSoup(deck_response.text, "html.parser")
inventory_soup = BeautifulSoup(inventory_response.text, "html.parser")
commander_soup = BeautifulSoup(commander_response.text, "html.parser")


#deck is a list of card names in your deck
deck = deck_soup.body.contents


#inventory is a list of card names you own
inventory = inventory_soup.body.contents

#fix up the lists so we can compare
del deck[1::2]
del inventory[1::2]
deck = [e[2:] for e in deck]
inventory = [e[2:] for e in inventory]

#cuts out the annoying leading white space from the deckbox text export's first row
deck[0] = deck[0].replace("       1 ","")
inventory[0] = inventory[0].replace("       1 ","")

#commander is a string of card names recommended by EDHREC
commander = commander_soup.find_all(class_='nwname')

comm_clean = []

#cleans up the commander set and produces plain strings with no markup or whitespace
for tag in commander:
	comm_clean.append(tag.text.strip())
	
potentials = []	

#adds cards to potentials that are cards EDHREC suggests and that you own
for card in inventory:
	if card in comm_clean:
		potentials.append(card)
	else:
		continue

recos = []
		
#filters out potentials based on cards that are already in the deck
for card in potentials:
	if card not in deck:
		recos.append(card)
	else:
		continue
		
#removes duplicates
recos = set(recos)

#prints the output
print ('[%s]' % '\n'.join(map(str, recos)))