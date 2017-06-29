from bs4 import BeautifulSoup as bs
import urllib2
import requests

def scrape_transcript(ticker):
    #site = "https://seekingalpha.com/search/transcripts?term={}&all=true".format(ticker)
    site = "https://seekingalpha.com/article/4042306-amazon-com-amzn-q4-2016-results-earnings-call-transcript?all=true&find=amzn"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers = hdr)
    page = urllib2.urlopen(req)
    soup = bs(page)
    return soup

if __name__ == "__main__":
    ticker = 'amzn'
    print scrape_transcript(ticker)
