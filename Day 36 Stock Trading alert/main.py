STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "65QOX3M3WH3GDG2A"
NEWS_API_KEY = "f48945d1eb6a4412bb4c881d85ec6673"

from datetime import date

import requests

today = date.today()

# print(daily_data)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
from twilio.rest import Client

account_sid = "ACbe627bb9983b5ce004bcd201522ec919"
auth_token = "514a0f962b0be7bdae58e6a260ea3803"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {

    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "function": "TIME_SERIES_DAILY"
}
data = requests.get(url=f"https://www.alphavantage.co/query", params=parameters).json()

daily_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in daily_data.items()]

yesterday = data_list[0]
day_before_yesterday = data_list[1]

yesterday_price = float(yesterday['4. close'])
day_before_yesterday_price = float(day_before_yesterday['4. close'])

diff = yesterday_price - day_before_yesterday_price
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percent = int((diff / day_before_yesterday_price) * 100)
if percent > 0:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "qInTitle": "Tesla",
        "from": today,
        "sortBy": "relevancy",
        "apiKey": NEWS_API_KEY,
        "pageSize": 3,
        "language": "en"
    }
    news_data = requests.get(
        url='https://newsapi.org/v2/everything', params=news_parameters).json()["articles"]
    three_articles = news_data[:3]
    formatted_articles = [f"\nHeadline:{article['title']}\nBrief:{article['description']}" for article in
                          three_articles]

    # STEP 3
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=f"{STOCK}: {up_down} {percent}%\n"
                 f"{article}",
            from_='+19543711080',
            to='+919773707840'
        )
        print(message.status)
