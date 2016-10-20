import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
from tweepy import Stream
from tweepy.streaming import StreamListener
#comment1 explain StreamListener() its important because it is used to customize the way we process the incoming data.
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('output_file_name.json', 'a') as f:     #create a json file and use that file in place of output_file_name
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
print('Enter hashtag to be extracted')
str1= input()
twitter_stream.filter(languages=["en"],track=[str1])  #languages=["en"] is for english tweets remove this if no language filter is required on tweets





