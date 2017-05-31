import urllib2
from BeautifulSoup import BeautifulSoup

##CONFIG
reset = 0 # 900=15mins
tweetTime = 300 # One min

def getHeadlines():
    page = urllib2.urlopen('http://mkdlc.ebanking.hsbc.com.hk/pws/pagecontent.jsp?id=1200&lang=en').read()
    soup = BeautifulSoup(page)
    from xml.sax.saxutils import unescape
    #for i in soup.findAll('span', {'class' : 'ellipsis_text'}):
        #print i.text
    news = []
    for i in soup.findAll('span', {'class' : 'ellipsis_text'}):
        news.append(i.text)
    #unescape(str(links[1]))
    a = (soup.findAll('div',id="newsContent"))
    links = []
    for line in a:
        for row in line.findAll('a', href=True):
            links.append(unescape(str(row)))
    return news, links

import tweepy, time, sys
#enter the correspondintang information from your Twitter application:
CONSUMER_KEY = '' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '' #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '' #keep the quotes, replace this with your access token
ACCESS_SECRET = '' #keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

import re
if __name__ == "__main__":
    for j in range(0, 999999):
        news = []
        links = []
        news, links = getHeadlines()
        links2 = []
        for i in range(0, len(links)-1):
            s = links[i]
            result = re.search('<a href="(.*)">\n', s)
            #print(str(str("POSTING THIS: " + news[i] + " " + "http://mkdlc.ebanking.hsbc.com.hk/pws/" + str(result.group(1)))))
            print("posted... post number: %s" %i)
            if(len(news[i]) <= 140):
                try:
                    api.update_status(str(news[i] + " " + "http://mkdlc.ebanking.hsbc.com.hk/pws/" + str(result.group(1))))
                except:
                    pass
                time.sleep(tweetTime)#Tweet every 20 seconds
        time.sleep(reset)#Tweet every 15 seconds
        
