from twython import Twython, TwythonError
from pprint import pprint

'''
Author: Eron Cemal
This is the start of an twitter chat bot. I want it to start search twitter for a 
hastag like "#testaskfullfact". It will then reply to that twitter

This is what I used as a start. it explains some things:
https://geekswipe.net/technology/computing/code-python-twitter-bot-in-ten-minutes/

then I moved on to

http://twython.readthedocs.io/en/latest/index.html


'''

if __name__ == "__main__":

    APP_KEY = ''
    APP_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
    
    SEARCH_HASHTAG = "#fullfact"  # maybe replace this with #askfullfact?
    BOT_TWITTER_NAME = "insert here"
    
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    results = twitter.search(q=SEARCH_HASHTAG)
    
    pprint(results["statuses"])  #this is all the statuses this is an array
    
    pprint(results["statuses"][0]["text"]) # this is the actual content for the first element
    
    # within these results, we want to ignore anything which is from user BOT_TWITTER_NAME
    
    # we want to ignore ones we already replied to. How? do we keep a local database of tweets replied to?
    
    # we might want to reply to tweets only within the last minute. How
    
    # update twitter with this 
#     twitter.update_status(status=line)