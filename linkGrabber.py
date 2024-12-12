#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Programmer

# [+] Enter the Target with the FQDN

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# to avoid duplicates
visited_urls = set()

def link_urls(url, keyword):
	# Checking the Target is UP or not
	try:
		response = requests.get(url)
	except:
		print(f"Request failed {url}")
		return

	# Using BeautifulSoup to grab html element
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')

		# Recusively finding all a tags
		a_tag = soup.find_all('a')
		urls = []
		for tag in a_tag:
			href = tag.get("href")
			if href is not None and href != "":
				urls.append(href)

		# For printing the URLs recusivly
		for urls2 in urls:
			if urls2 not in visited_urls:
				visited_urls.add(urls2)
				url_join = urljoin(url, urls2)
				if keyword in url_join:
					print(url_join)
					link_urls(url_join, keyword)


url = input("Enter the URL you want to scrap. ")
keyword = input("Enter the keyword to search for in the URL provided. ")
link_urls(url, keyword)