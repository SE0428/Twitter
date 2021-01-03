from tweepy import OAuthHandler
import tweepy
import pandas as pd
import os
import time

# Twitter credentials
# Obtain them from your twitter developer account
consumer_key = "VwCBrL8tr9vZFrstpQx9Jd8Lw"
consumer_secret ="zLLsjUDP7O6H2CAESaBkNVbFwywDbvyc9J5bUsmEmo5MAFQkB6"
access_key = "1246017810829963266-Z4lRoe6vgvavBQ5l81l0IllKUWwye4"
access_secret = "xufcdZ38Man62KDZbq0fWsVCgIWIYr00u5gwtAc9lzGWQ"

#consumer_key = "XdYStjaa6zqGAseZN1Xe0Ge8c"
#consumer_secret ="tgJJW8DPB3Nr6c9lnSC6PxyUEfUSdo5cDVIINLfImAgl2M3HX6"
#access_key = "1246036379491950593-hNyHUfcjIHvqR8Z5DZpsekhHSJelMU"
#access_secret = "2i2RPjgzOlJOwdIsHwxJQTDHUzoPrqyzkQBlDkefLZdon"


# Pass your twitter credentials to tweepy via its OAuthHandler
auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, timeout=300)


def scraptweets(search_words, date_since, numTweets, numRuns):
    # Define a for-loop to generate tweets at regular intervals
    # We cannot make large API call in one go. Hence, let's try T times

    # Define a pandas dataframe to store the date:
    db_tweets = pd.DataFrame(columns=['username', 'acctdesc', 'location', 'following',
                                      'followers', 'totaltweets', 'usercreatedts', 'tweetcreatedts',
                                      'retweetcount', 'text', 'hashtags']
                             )
    program_start = time.time()
    for i in range(0, numRuns):
        # We will time how long it takes to scrape tweets for each run:
        start_run = time.time()

        # Collect tweets using the Cursor object
        # .Cursor() returns an object that you can iterate or loop over to access the data collected.
        # Each item in the iterator has various attributes that you can access to get information about each tweet
        tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since, tweet_mode='extended').items(numTweets)

        # Store these tweets into a python list
        tweet_list = [tweet for tweet in tweets]
        #print(tweet_list)

        # Obtain the following info (methods to call them out):
        # user.screen_name - twitter handle
        # user.description - description of account
        # user.location - where is he tweeting from
        # user.friends_count - no. of other users that user is following (following)
        # user.followers_count - no. of other users who are following this user (followers)
        # user.statuses_count - total tweets by user
        # user.created_at - when the user account was created
        # created_at - when the tweet was created
        # retweet_count - no. of retweets
        # (deprecated) user.favourites_count - probably total no. of tweets that is favourited by user
        # retweeted_status.full_text - full text of the tweet
        # tweet.entities['hashtags'] - hashtags in the tweet
        # Begin scraping the tweets individually:
        noTweets = 0


        for tweet in tweet_list:
            # Pull the values
            username = tweet.user.screen_name
            acctdesc = tweet.user.description
            location = tweet.user.location
            following = tweet.user.friends_count
            followers = tweet.user.followers_count
            totaltweets = tweet.user.statuses_count
            usercreatedts = tweet.user.created_at
            tweetcreatedts = tweet.created_at
            retweetcount = tweet.retweet_count
            hashtags = tweet.entities['hashtags']
            try:
             text = tweet.retweeted_status.full_text
            #print(text)
            except AttributeError:  # Not a Retweet
              text = tweet.full_text
             #print(text)


            # Add the 11 variables to the empty list - ith_tweet:
            ith_tweet = [username, acctdesc, location, following, followers, totaltweets,
                usercreatedts, tweetcreatedts, retweetcount, text, hashtags]

            db_tweets.loc[len(db_tweets)] = ith_tweet
             # increase counter - noTweets
            noTweets += 1

            # Run ended:
            end_run = time.time()
            duration_run = round((end_run - start_run) / 60, 2)

                    #filename = 'hey.csv'
            #db_tweets.to_csv(filename, index=False)

        print('no. of tweets scraped for run {} is {}'.format(i + 1, noTweets))
        print('time take for {} run to complete is {} mins'.format(i + 1, duration_run))

        time.sleep(150)  # 3 minute sleep time
    # Once all runs have completed, save them to a single csv file:
    path = os.getcwd()
    filename ='2019_12_18_family.csv'
    print(search_words)
    print(filename)

    # Store dataframe in csv with creation date timestamp

    db_tweets.to_csv(filename, index=False)


    program_end = time.time()
    print('Scraping has completed!')
    print('Total time taken to scrap is {} minutes.'.format(round(program_end - program_start) / 60, 2))

# Initialise these variables:
print("tweepy works")
#search_words = "#country OR #capital OR #currency"
#search_words= "#capital city OR city"
search_words= "#family OR #mother OR #father OR #brother OR #sister" #family
#search_words= "#man OR #king OR #queen OR #boy OR #girl" #family2
#search_words="#baht OR #yen OR #dollar OR #euro OR #ruble OR #peso OR #rupee "
#search_words="#USD or #HKD OR #WON OR #INR OR #CNY OR #RMB" #currency2


date_since = "2019-12-18"
numTweets = 500
numRuns = 10

print(date_since)

#Call the function scraptweets

scraptweets(search_words, date_since, numTweets, numRuns)
