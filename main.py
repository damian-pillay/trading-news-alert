import requests
from twilio.rest import Client
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

### 
# Note: 
# alphavantage only has data from the previous day onward
# the code only works from 6am to midnight
# the reason is because from midnight to 6am, 
# its a new day in south africa, but its still the previous day in america
# hence, you will get an error because data for the previous does not exist yet"
###

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
day_before_yest = yesterday - datetime.timedelta(days=1)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

AV_API = os.environ["AV_API"]
AV_API_KEY = os.environ["AV_API_KEY"]

NEWSAPI = os.environ["NEWSAPI"]
NEWSAPI_KEY = os.environ["NEWSAPI_KEY"]

account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_TOKEN"]
my_number = os.environ["MY_NUMBER"]
twilio_number = os.environ["TWILIO_NUMBER"]

av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}

news_params = {
    "q": "tesla",
    "searchIn": "title",
    "from": day_before_yest,
    "to": yesterday,
    "language": "en",
    "pageSize": 3,
    "apiKey": NEWSAPI_KEY
}

response = requests.get(url=AV_API, params=av_params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]

stock_yest = float(data[f"{yesterday}"]["4. close"])
stock_day_before_yest = float(data[f"{day_before_yest}"]["4. close"])

percentage_change = ((stock_yest - stock_day_before_yest)/stock_day_before_yest) * 100
change_symbol = "🔺"

if percentage_change < 0:
    increase = "🔻"
    percentage_change *= -1

if percentage_change > 2:

    news_response = requests.get(url=NEWSAPI, params=news_params)
    news_response.raise_for_status()

    articles = news_response.json()["articles"]

    message = f"""
    {STOCK}: {change_symbol} {round(percentage_change)}%
    Headline: {articles[0]["title"]}
    Brief: {articles[0]["description"]}

    Headline: {articles[1]["title"]}
    Brief: {articles[1]["description"]}

    Headline: {articles[2]["title"]}
    Brief: {articles[2]["description"]}
    """

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=twilio_number,
        body = message,
        to=my_number
    )