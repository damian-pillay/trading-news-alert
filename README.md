# Stock Alert App

## 1. Introduction
The Stock Alert App monitors stock price changes and sends notifications via SMS if significant changes are detected. It uses the Alpha Vantage API to fetch stock data and the News API to retrieve related news articles. Notifications are sent using the Twilio API.

## 2. Features
- Fetches daily stock price data for a specified stock symbol.
- Compares stock prices between consecutive days.
- Retrieves recent news articles related to the stock.
- Sends an SMS alert if the stock price change exceeds a specified threshold.

## 3. Technologies Used
- **Python**: The programming language used for the app.
- **Requests**: For making HTTP requests to APIs.
- **Alpha Vantage API**: Provides stock price data.
- **News API**: Retrieves related news articles.
- **Twilio API**: Sends SMS notifications.
- **dotenv**: Manages environment variables.

## 4. Setup and Installation
### Prerequisites
- Python 3.x
- Twilio account
- Alpha Vantage API key
- News API key

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/trading-news-alert.git
    ```
2. Navigate to the project directory:
    ```bash
    cd stock-alert-app
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the root directory and add your environment variables:
    ```ini
    AV_API=https://www.alphavantage.co/query
    AV_API_KEY=your_alpha_vantage_api_key
    NEWSAPI=https://newsapi.org/v2/everything
    NEWSAPI_KEY=your_news_api_key
    TWILIO_SID=your_twilio_account_sid
    TWILIO_TOKEN=your_twilio_auth_token
    MY_NUMBER=your_phone_number
    TWILIO_NUMBER=your_twilio_phone_number
    ```

## 5. Usage
1. Run the script:
    ```bash
    python stock_alert.py
    ```
2. The script will fetch the stock data and news, then send an SMS alert if the stock price change exceeds the threshold.

## 6. Challenges and Limitations
- **API Data Availability**: Alpha Vantage only provides data from the previous day, so the app only works between 6 am and midnight.
- **Time Zone Issues**: The app's functionality is limited by time zone differences between South Africa and the U.S.

## 7. Future Development
- Implement a more dynamic configuration for stock symbols and thresholds.
- Add support for multiple stock symbols and alert criteria.
- Enhance error handling and logging.

## 8. License
This project is not licensed and is therefore protected by copyright. All rights are reserved to the author. You may not use, distribute, or modify this code without explicit permission.

## 9. Contact
- **Name**: Damian Lee Pillay
- **Email**: damianleep@gmail.com
- **GitHub**: [damian-pillay](https://github.com/damian-pillay)
