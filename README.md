# Robinhood Day Trading (w/ sentiment analysis)

<pre>
structure:

    dataScrape.py       <- script for scraping news, prices, etc. during trading hours
      |
    data/
      |______ pooled.csv      <- location to dump data from dataScrape
      |
    dayLoop.py          <- script for executing trading logic during day
      |
    utils.py            <- utility functions for project
      |
    models/
      |______ sentiment.py    <- contains nn architecture for sentiment analysis
      |
      |______ train.py        <- contains training loop for sentiment analysis model
      |
    scratchBooks/       
      |______ ...       <- scratch space for prototyping functions in jupyter
      |______ ...
      
 </pre>

  
