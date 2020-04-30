import tweepy
import csv

#Twitter API key �iTwitter API�\�����ɏ����ł���l�I�ȃL�[�Ax�ɃL�[�������j
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

#API�F��
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#�c�C�[�g�擾

#list�����
tweet_data = []

#items(n) n�������c�C�[�g��
for tweet in tweepy.Cursor(api.user_timeline,screen_name = "chiisann_",exclude_replies = True).items(100): #screen_name��@��������Twitter�A�J�E���g��
	if not "RT" in tweet.text:
    	tweet_data.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])

#csv�o��
with open('tweets_2020042901.csv', 'w',newline='',encoding='utf-8') as f: #open()�Ńt�@�C�����̎w��
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","fav","RT"])#5�����
    writer.writerows(tweet_data)