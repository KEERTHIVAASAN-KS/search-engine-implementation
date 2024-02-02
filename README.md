search-engine-implementation is an implementation of search engine which crawls through web through the seed urls and gives the search results

crawler.py in crawl_bot directory crawls through web

searchengine.py searches from crawled websites and ranks all the websites based on searchstring given

USAGE:

enter "pip install -r requirements.txt" 

enter the seedurls in crawllist.txt (each url in a line) ,without this step the crawler.py does not crawl through web

to run crawler.py enter "python crawler.py" 

 to run searchengine.py enter "python searchengine.py searchstring" 

REQUIREMENTS:

python

pip

