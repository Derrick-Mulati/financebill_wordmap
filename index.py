import tweepy
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Step 1: Authenticate to Twitter
api_key = "YOUR_API_KEY"
api_key_secret = "YOUR_API_KEY_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Set up the tweepy client
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Step 2: Collect Tweets
query = "Finance Bill 2024"  # Query term
tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(500)

# Store the tweets in a list
tweets_list = [tweet.full_text for tweet in tweets]

# Step 3: Create a DataFrame
df = pd.DataFrame(tweets_list, columns=["Tweets"])

# Step 4: Text Cleaning
def clean_text(text):
    # Remove mentions, hashtags, links, and special characters
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'\W+', ' ', text)
    return text

df['Tweets'] = df['Tweets'].apply(clean_text)

# Step 5: Generate Word Cloud
all_words = ' '.join([text for text in df['Tweets']])
wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110, background_color='white').generate(all_words)

# Step 6: Visualize the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()
