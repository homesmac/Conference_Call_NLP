# Conference-Call-Project

“What I really meant to say was…”

This project is not designed to predict a company’s performance in the stock market. The business understanding I plan on gathering is based on company XYZ’s projected financial figures and perhaps more importantly, the choice, sentiment, and frequency of words used on a XYZ’s quarterly earnings conference call, can I predict how their next quarter’s figures will differ than those proposed. There is a subtle difference between this and predicting how their stock will perform. I don’t want to try to predict XYZ being up 5% next quarter based on this conference call, rather I want to be able to predict XYZ’s revenue growth being 6% as opposed to the company’s forecast of 7%. This is an important distinction because this has a much better chance of being viable as opposed to predicting a stock price in which many more factors are considered. Since there are many financial figures forecasted in a company’s conference call, I will narrow the project’s focus to predicting the next quarter’s revenue. 

I will implement tf-idf to gain insight into each words’ overall importance to the corpus. My corpus will consist of the conference call transcripts' spoken words.

I will also apply a NaiveBayesClassifier using NLTK to classify each word as positive or negative. Each conference call would end up being classified into positive or negative and to a certain degree, which I can then use to adjust the revenue figure proposed by the company.


Source: https://seekingalpha.com/earnings/earnings-call-transcripts

