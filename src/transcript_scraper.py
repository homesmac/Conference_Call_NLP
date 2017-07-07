from bs4 import BeautifulSoup as bs
import urllib2
import requests
import re
import time
import json
from random import randint
from collections import defaultdict
import sqlalchemy
from sqlalchemy import *
import MySQLdb
from splinter import Browser
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options

# from pymongo import MongoClient

conference_call_links = []
def generate_transcript_links(ticker):
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    print ticker
    print '=================================='
    site = "https://seekingalpha.com/symbol/{}/earnings".format(ticker)
    chromedriver = "/Users/homes/Downloads/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    r = driver.get(site)

    # executable_path = {'executable_path':'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'}

    # browser = Browser(driver)
    time.sleep(randint(7,10))
    driver.find_element_by_id("sub-menu-transcripts").click()
    time.sleep(randint(7,10))
    #site = "https://seekingalpha.com/article/4042306-amazon-com-amzn-q4-2016-results-earnings-call-transcript?all=true&find=amzn"
    # bssite = browser.html.encode('utf-8')
    # hdr = {'User-Agent': 'Google Chrome'}
    # req = urllib2.Request(site, headers = hdr)
    # page = urllib2.urlopen(req)

    earnings_links = driver.find_elements_by_xpath("//a[contains(@href,'results-earnings-call-transcript')]")
    for i in earnings_links:
        conference_call_link = i.get_attribute("href")+'?part=single'
        h.write('{0},{1}'.format(ticker, conference_call_link))
        h.write('\n')

        # conference_call_links.append(confere_call_link)

    driver.close()
###########################commented out below to just get links
#     print soup
#     transcript_links = [div.a for div in soup.findAll("div", attrs={ "class" : "symbol_article"})]
#     #print transcript_links.select("a[href*=results-earnings-call-transcript]")
#     print transcript_links
#     ind_calls = []
#     call_dict = defaultdict(list)
#     for link in transcript_links:
#         earnings_links = soup.find_all('a', href=re.compile("results-earnings-call-transcript"))
#     for i in earnings_links:
#         full_link = 'https://seekingalpha.com' + i['href'] + '?part=single'

#         response = requests.get(full_link, headers = hdr)
#         data = response.text
#         # ind_calls.append((ticker, data))
#     # for ticker,html in ind_calls:
#     #     call_dict[ticker].append(html)
#     # asdg.insert_one(call_dict)
# #def html_scrape(link):
#     # [h.write('{0},{1}'.format(key, value)) for key, value in call_dict]

#     # db = MySQLdb.connect("localhost","root","vvocaL)0","INNERMARGIN" )
#     # cursor = db.cursor()
#     i = Transcripts.insert()
#     i.execute({'Ticker': ticker, 'Revenue': revenue, 'Calls': data})
#     db.commit()
######################################


if __name__ == "__main__":
    #####################################
    # db = create_engine('mysql+mysqldb://root:vvocaL)0@localhost/confcalls')
    # metadata = MetaData(db)
    # Transcripts = Table('Transcripts', metadata,
    #         Column('Ticker', primary_key=True),
    #         Column('Revenue', String()),
    #         Column('Calls', String())
    #         )
    # try:
    #     Transcripts.create()
    # except:
    #     pass
    ############################################
    # db = MongoClient('mongodb://localhost:27017/')['conference_call_project']
    # asdg = db.conference_calls

    with open('../data/stocktickers.txt', 'r') as f:
        with open('../data/html_dict2.csv', 'w') as h:
            for ticker in f:

                time.sleep(randint(7,10))

                generate_transcript_links(ticker.replace('\n',''))

#results-earnings-call-transcript

#https://seekingalpha.com

#?part=single
