import tweepy
import datetime
import os
import socket
import time
#AI Agent X Post - Daily Motivational Quote
# Step 1: Wait for internet connection (try for up to 2 minutes)
def is_connected():
    try:
        socket.create_connection(("api.twitter.com", 443), timeout=5)
        return True
    except OSError:
        return False

for _ in range(120):  # wait max 2 mins (120 seconds)
    if is_connected():
        break
    time.sleep(1)
else:
    print("❌ Internet not available. Tweet not sent.")
    exit()

# Step 2: Check if already posted today
today = datetime.datetime.now().strftime("%Y-%m-%d")
weekday = datetime.datetime.now().strftime("%A")

log_file = "last_posted.txt"
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        last_date = f.read().strip()
    if last_date == today:
        print("✅ Already posted today. Skipping.")
        exit()

# Step 3: Tweet today's quote
quotes = {
    "Monday": "Believe in yourself.",
    "Tuesday": "Work hard, Pray, Hustle.",
    "Wednesday": "Strain for Success.",
    "Thursday": "Stay positive, Strive for the best.",
    "Friday": "Everything is possible.",
    "Saturday": "Enjoy Life.",
    "Sunday": "Make yourself proud."
}
quote = quotes.get(weekday, "Stay inspired.")

# Twitter credentials
API_KEY = "Y8C1iYETw2LBZXK5Fexbma3wV"
API_SECRET_KEY = "49PvNib1D07JTCCY7q2RbNiN8ZXNpoYGkcRjGRvELjYPdseRDm"
ACCESS_TOKEN = "1478106306124865537-xjMpEumULPB31qohK4sZ8fRmCVXAe5"
ACCESS_TOKEN_SECRET = "0Hwt85Wj4c1f2xYgAkmJy9aZPUGQtJD1FEdy2e1VBovPZ"


# Step 4: Post the tweet
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

try:
    response = client.create_tweet(text=quote)
    print(f" Posted: {quote}")
    with open(log_file, "w") as f:
        f.write(today)
except Exception as e:
    print(f" Failed to post tweet: {e}")