#!/usr/bin/python

import os, subprocess
from html.parser import HTMLParser
from pprint import pprint

#choose your own google books search terms
searcharr=[
"ballerina said",
"catacombs",
"conflagration",
"covert",
"factotum",
"girl with the",
"his mantra",
"private banker",
"inadequate personality",
"medicine",
"looting spread",
"murmured",
"mystery blaze",
"offering",
"poured in",
"mask",
"puzzledover",
"took off",
"ultra-affluent",
"was her doctor"]

#after creating directories for manually downloaded google books search results pages, list them here
dirarr=[
"ballerinasaid",
"catacombs",
"conflagration",
"covert",
"factotum",
"girlwiththe",
"hismantra",
"hisprivatebanker",
"inadequatepersonality",
"jarmedicine",
"lootingspread",
"murmured",
"mysteryblaze",
"offering",
"pouredin",
"purplish",
"putonmask",
"puzzledover",
"tookoffmask",
"ultra-affluent",
"washerdoctor"]

rootdir="**YOURROOTDIRECTORYHERE**"

def srch(rootdir, directory, term, parser):
	#output = ""
	for filen in os.listdir(rootdir+"/"+directory):
		if filen.endswith(".html"):
			with open(rootdir+"/"+directory+"/"+filen) as page:
				for line in page:
					if "<em>" in line:
						line=line[0:line.find("<em>")]+line[line.find("<em>")+4:]
					if "</em>" in line:
						line=line[0:line.find("</em>")]+line[line.find("</em>")+5:]
					parser.feed(line)
		else: pass
		
#for google books, "fl" is class for <a href> tag including link to book
#"st" is attribute for the span tag including the search term
#the search term is tagged with <em>
#we want a sentence within the span that has the em tag
#within span; if span contains <em>; back up to first capital letter; store everything from that to the first (period, space, capital letter)	

class MyHTMLParser(HTMLParser):

	localstore = {}		

	def handle_data(self, data):
		if "span" in self.get_starttag_text():
			if "st" in self.get_starttag_text():
				print(data)

		if "em" in self.get_starttag_text():
   				print(data)

parser = MyHTMLParser()

#main function call
for directory in dirarr:
	for term in searcharr:
		srch(rootdir, directory, term, parser)

