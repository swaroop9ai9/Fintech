# The program states wheather buying a particular stock is good or bad based on tweet's polarity of the stock and last year's stock performance. 

* Stock investment recommendations based on Machine Learning predictions from last year's values of any market symbol and also based on Twitter sentiment analysis from retrieved tweets containing the symbol as text inside of it.
* The Twitter sentiment analysis starts and it retrieves a list of the last 10000 tweets posted in english containing the
  symbol introduced and they are later stored in a list of Tweet class, defined in Tweet.py with the tweet's text and polarity 
  from TextBlob.
  
  sample o/p:
Retrieving GOGL related tweets polarity...
Generating recommendation based on prediction & polarity...
According to the predictions and twitter sentiment analysis -> Investing in GOGL is a GREAT idea!
