# Conference_Call_NLP

“What I really meant to say…”

# Business Understanding
Can we predict whether companies will hit or miss their projected quarterly revenue based on the contents of their earnings conference calls?

# Why?
Revenues are important!
* Is the company allocating capital efficiently?
* Are consumers BUYING their products? (iPhone -vs- Fire Phone)
* Debt financing! Lower debt to equity ratio >> lower interest rates

# Data
* S&P 500 companies
* 5,320 conference calls
* Roughly 60,000,000 words
* Avg call length: 58,000 words
* Analyzes past 6 quarters (avg)

# Data Prepartion
* Scrape transcripts
* Isolate revenue performance
* TF-IDF Vectorizer on transcripts
* Preprocessed using LabelEncoder
* Assign sentiment using NLTK’s Vader module

# Feature Engineering
* Sentiment (Vader)
* Current quarter
* Length of call
* Last quarter’s performance

# Key Sentiment Findings
Conference calls are boring!
* 85% neutral
* 13% positive
* 2% negative

# Evaluation - Does it work?
55% of companies beat revenue on average

Accuracy scores
* Multinomial Naive Bayes: 0.586
* Gradient Boosted Classifier: 0.597
* Logistic Regression: 0.623
* Ensemble of GBC and LR: 0.646

# Live Performance as of 7/19/2017
| Ticker | Predict | Actual |
| ------------- | ------------- |--------|
| BAC | Miss | Beat | 
| BLK | Miss | Miss | 
| C | Miss | Beat |  
| DAL | Miss | Miss |  
| FAST | Miss | Beat | 
| GS | Beat | Beat |  
| GWW | Miss | Miss |  
| HOG | Miss | Miss |  
| JNJ | Beat | Miss |  
| JPM | Beat | Beat |  
| LMT | Beat | Beat |  
| MS | Beat | Beat |  
| MTB | Beat | Beat |  
| NFLX | Miss | Beat |  
| NTRS | Miss | Beat | 
| PEP | Beat | Beat |  
| PGR | Miss | Miss |  
| PNC | Beat | Beat |  
| TXT | Miss | Miss |  
| UNH | Beat | Miss |  
| USB | Beat | Beat | 
| WFC | Miss | Miss | 

Live accuracy score:  68.2%

# Next Steps
* Train using EPS in addition to revenue
* Implement additional models to predict degree of hit/miss on revenues

# Contact
Jonathan McWilliams
jonathan dot g dot mcwilliams at gmail
linkedin.com/in/jonathan-mcwilliams

Source: https://seekingalpha.com/earnings/earnings-call-transcripts

