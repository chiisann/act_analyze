import tweepy
import csv

#Twitter API key （Twitter API申請時に所得できる個人的なキー、xにキーをいれる）
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

#API認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#ツイート取得

#listを作る
tweet_data = []

#items(n) nが所得ツイート数
for tweet in tweepy.Cursor(api.user_timeline,screen_name = "chiisann_",exclude_replies = True).items(100): #screen_nameに@を除いたTwitterアカウント名
	if not "RT" in tweet.text:
    	tweet_data.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])

#csv出力
with open('tweets_2020042901.csv', 'w',newline='',encoding='utf-8') as f: #open()でファイル名の指定
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","fav","RT"])#5列つくる
    writer.writerows(tweet_data)