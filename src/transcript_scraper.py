from bs4 import BeautifulSoup as bs
import urllib2
import requests
import re
import time
import json
from random import randint
from collections import defaultdict
from pymongo import MongoClient

def generate_transcript_links(ticker):
    print ticker
    print '=================================='
    site = "https://seekingalpha.com/symbol/{}/earnings/transcripts".format(ticker)

    #site = "https://seekingalpha.com/article/4042306-amazon-com-amzn-q4-2016-results-earnings-call-transcript?all=true&find=amzn"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers = hdr)
    page = urllib2.urlopen(req)
    soup = bs(page)
    transcript_links = [div.a for div in soup.findAll("div", attrs={ "class" : "symbol_article"})]
    #print transcript_links.select("a[href*=results-earnings-call-transcript]")

    ind_calls = []
    call_dict = defaultdict(list)
    for link in transcript_links:
        earnings_links = soup.find_all('a', href=re.compile("results-earnings-call-transcript"))
    for i in earnings_links:
        full_link = 'https://seekingalpha.com' + i['href'] + '?part=single'

        response = requests.get(full_link, headers = hdr)
        data = response.text
        ind_calls.append((ticker, data))
    for ticker,html in ind_calls:
        call_dict[ticker].append(html)
    print call_dict
    asdg.insert_one(call_dict)
#def html_scrape(link):


if __name__ == "__main__":
    db = MongoClient('mongodb://localhost:27017/')['conference_call_project']
    asdg = db.conference_calls

    with open('data/stocktickers.txt', 'r') as f:
        for ticker in f:

            time.sleep(randint(5,7))
            generate_transcript_links(ticker.replace('\n',''))

#results-earnings-call-transcript

#https://seekingalpha.com

#?part=single
