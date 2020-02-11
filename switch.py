#!/usr/bin/env python
# coding: utf-8

# In[54]:


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[55]:


atoken = "1192180647995019264-I1u63JAoclo1g1ROx9N3OcNJgH50j4"
asecret = "qTl1sVDKue8SBUIk5EWSZJTk3bGrz1ZlLaTSvHSpWGntv"
ckey = "43sK4N35IgMibtFp9uPdAA8V2"
csecret = "8W7RcprxImVjhjR5Z7UQn5BFYb6yAhZVsx1qly0Kcjaq2Ee1MA"


# In[56]:


#Create a class inheriting from StreamListener
class listener(StreamListener):
    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet1 = all_data["text"]
            tweet = tweet1.encode('UTF-8')
            location = all_data["user"]["location"]
            #location = location1.encode('UTF-8')
            username = all_data["user"]["screen_name"]
            #username = username1.encode('UTF-8')
            id_str = all_data["user"]["id_str"]
            followers_count = all_data["user"]["followers_count"]
            friends_count = all_data["user"]["friends_count"]
            favourites_count = all_data["user"]["favourites_count"]
            time_zone = all_data["user"]["time_zone"]
            #time_zone = time_zone1.encode('UTF-8')

            out = open('11.19switch.csv', 'a')
            out.write(str(username)+'::'+str(followers_count)+'::'+str(location)+'::'+str(tweet))
            out.write('\n')
            out.close()
            print (username, " :: ", tweet, " :: ",location)
        except :
            print ('failed ondata')


    def on_error(self, status):
        print (status)


# In[57]:


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
keywords = ["switch"]
twitterStream = Stream(auth, listener())
twitterStream.filter(track=keywords, languages=["en"])


# In[63]:


import pandas as pd
df = pd.read_csv('11.19switch.csv', sep = '::', engine = 'python', header = None,names = ['user screen name','number of followers','location','tweet text'])
df.head()
df.to_csv('switch.csv')


# In[ ]:




