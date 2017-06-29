from bs4 import BeautifulSoup as bs
import urllib2
import requests
import re

def scrape_transcript(ticker):

    site = "https://seekingalpha.com/search/transcripts?term={}&all=true".format(ticker)
    #site = "https://seekingalpha.com/article/4042306-amazon-com-amzn-q4-2016-results-earnings-call-transcript?all=true&find=amzn"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers = hdr)
    page = urllib2.urlopen(req)
    soup = bs(page)
    transcript_links = [div.a for div in soup.findAll("div", attrs={ "class" : "transcript_link"})]
    #print transcript_links.select("a[href*=results-earnings-call-transcript]")
    for link in transcript_links:
        earnings_links = soup.find_all('a', href=re.compile("results-earnings-call-transcript"))
    for i in earnings_links:
        print i


if __name__ == "__main__":
    ticker = 'msft'
    scrape_transcript(ticker)

#results-earnings-call-transcript
