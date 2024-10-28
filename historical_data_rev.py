from fyers_apiv3 import fyersModel

"""
In order to get started with Fyers API we would like you to do the following things first.
1. Checkout our API docs :   https://myapi.fyers.in/docsv3
2. Create an APP using our API dashboard :   https://myapi.fyers.in/dashboard/

Once you have created an APP you can start using the below SDK
"""

#### Generate an authcode and then make a request to generate an accessToken (Login Flow)

"""
1. Input parameters
"""

FY_ID = "XJ05073"
TOTP_KEY = "J2QYNE3IE2WSGWWG7L4S66ZUCM4GIIP7"
PIN = "1107"

redirect_uri = "http://127.0.0.1:5000"  ## redircet_uri you entered while creating APP.
client_id = "TGAOLE31HM-100"  ## Client_id here refers to APP_ID of the created app
secret_key = "I7W3ECL7MC"  ## app_secret key which you got after creating the app

grant_type = (
    "authorization_code"  ## The grant_type always has to be "authorization_code"
)
response_type = "code"  ## The response_type always has to be "code"
state = "sample"  ##  The state field here acts as a session manager. you will be sent with the state field after successfull generation of auth_code


## Connect to the sessionModel object here with the required input parameters
appSession = fyersModel.SessionModel(
    client_id=client_id,
    redirect_uri=redirect_uri,
    response_type=response_type,
    state=state,
    secret_key=secret_key,
    grant_type=grant_type,
)

# ## Make  a request to generate_authcode object this will return a login url which you need to open in your browser from where you can get the generated auth_code
generateTokenUrl = appSession.generate_authcode()
# print(generateTokenUrl)

from datetime import datetime, timedelta, date
from time import sleep
import os
import pyotp
import requests
import json
import math
import pytz
from urllib.parse import parse_qs, urlparse
import warnings
import pandas as pd

pd.set_option("display.max_columns", None)
warnings.filterwarnings("ignore")

import base64


def getEncodedString(string):
    string = str(string)
    base64_bytes = base64.b64encode(string.encode("ascii"))
    return base64_bytes.decode("ascii")


URL_SEND_LOGIN_OTP = "https://api-t2.fyers.in/vagator/v2/send_login_otp_v2"
res = requests.post(
    url=URL_SEND_LOGIN_OTP, json={"fy_id": getEncodedString(FY_ID), "app_id": "2"}
).json()
# print(res)

if datetime.now().second % 30 > 27:
    sleep(5)
URL_VERIFY_OTP = "https://api-t2.fyers.in/vagator/v2/verify_otp"
res2 = requests.post(
    url=URL_VERIFY_OTP,
    json={"request_key": res["request_key"], "otp": pyotp.TOTP(TOTP_KEY).now()},
).json()
# print(res2)


ses = requests.Session()
URL_VERIFY_OTP2 = "https://api-t2.fyers.in/vagator/v2/verify_pin_v2"
payload2 = {
    "request_key": res2["request_key"],
    "identity_type": "pin",
    "identifier": getEncodedString(PIN),
}
res3 = ses.post(url=URL_VERIFY_OTP2, json=payload2).json()
# print(res3)


ses.headers.update({"authorization": f"Bearer {res3['data']['access_token']}"})


TOKENURL = "https://api-t1.fyers.in/api/v3/token"
payload3 = {
    "fyers_id": FY_ID,
    "app_id": client_id[:-4],
    "redirect_uri": redirect_uri,
    "appType": "100",
    "code_challenge": "",
    "state": "None",
    "scope": "",
    "nonce": "",
    "response_type": "code",
    "create_cookie": True,
}

res3 = ses.post(url=TOKENURL, json=payload3).json()
# print(res3)


url = res3["Url"]
# print(url)
parsed = urlparse(url)
auth_code = parse_qs(parsed.query)["auth_code"][0]
# print(auth_code)

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type,
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token()

# Print the response, which should contain the access token and other details
# print(response)


## There can be two cases over here you can successfully get the acccessToken over the request or you might get some error over here. so to avoid that have this in try except block
try:
    access_token = response["access_token"]
except Exception as e:
    print(
        e, response
    )  ## This will help you in debugging then and there itself like what was the error and also you would be able to see the value you got in response variable. instead of getting key_error for unsuccessfull response.


# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(
    client_id=client_id, is_async=False, token=access_token, log_path=os.getcwd()
)
import pandas as pd
from datetime import datetime, timedelta

# Function to fetch data from Fyers API
def fetch_data(start_timestamp, end_timestamp, symbol="NSE:NIFTYBANK-INDEX"):
    data_requested = {
        "symbol": symbol,
        "resolution": "1",  # 1-minute data
        "date_format": "0",
        "range_from": start_timestamp,
        "range_to": end_timestamp,
        "cont_flag": "1",
    }
    
    try:
        res = fyers.history(data_requested)  # Make request to Fyers API
        return res["candles"]  # Extract candles data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []  # Return empty if there's an error

# Function to process the fetched data
def process_data(df_historical_data):
    df_historical_data["date"] = pd.to_datetime(
        df_historical_data["date"], unit="s", utc=True
    ).dt.tz_convert("Asia/Kolkata")  # Convert to IST time zone

    prev_day = None
    avg = 0
    daywise_results = []
    
    high_count = 0
    low_count = 0
    crossover_count = 0

    # Trade tracking
    trade_positive = 0  # Tracks crossover up
    trade_negative = 0  # Tracks crossover down
    trade_value_before_crossover = 0
    trade_value_after_crossover = 0
    trade_value_no_crossover = 0

    for i in range(1, len(df_historical_data)):
        current_date = df_historical_data["date"].iloc[i].strftime("%Y-%m-%d")
        close_value = df_historical_data["close"].iloc[i]

        if prev_day != current_date:  # Start of a new day
            open_value = df_historical_data["open"].iloc[i]
            high_value = df_historical_data["high"].iloc[i]
            low_value = df_historical_data["low"].iloc[i]
            volume_value = df_historical_data["volume"].iloc[i]

            if prev_day is not None:  # Skip first iteration (no prev_day)
                # Store the previous day's data
                daywise_results.append({
                    "date": prev_day,
                    "open": df_historical_data["open"].iloc[i - 1],
                    "close": df_historical_data["close"].iloc[i - 1],
                    "high": df_historical_data["high"].iloc[i - 1],
                    "low": df_historical_data["low"].iloc[i - 1],
                    "volume": df_historical_data["volume"].iloc[i - 1],
                    "above_average_count": high_count,
                    "below_average_count": low_count,
                    "crossover_count": crossover_count,
                    "trade_positive": trade_positive,
                    "trade_negative": trade_negative,
                    "trade_before_crossover": trade_value_before_crossover,
                    "trade_after_crossover": trade_value_after_crossover,
                })

            # Reset counters for the new day
            avg = (high_value + low_value) / 2  # Average of high and low
            high_count = 0
            low_count = 0
            crossover_count = 0
            trade_positive = 0
            trade_negative = 0
            trade_value_before_crossover = 0
            trade_value_after_crossover = 0
            prev_day = current_date
            continue

        # Count values above or below average
        if close_value > avg:
            high_count += 1
        elif close_value < avg:
            low_count += 1

        # Crossover logic and trade calculation
        prev_close_value = df_historical_data["close"].iloc[i - 1]
        if crossover_count < 3:
            if prev_close_value < avg and close_value > avg:
                crossover_count += 1  # Crossover up
                trade_positive += 1
                trade_value_after_crossover += close_value - prev_close_value
            elif prev_close_value > avg and close_value < avg:
                crossover_count += 1  # Crossover down
                trade_negative += 1
                trade_value_after_crossover += prev_close_value - close_value
            else:
                trade_value_before_crossover += close_value - prev_close_value

    # Capture the last day's data
    daywise_results.append({
        "date": current_date,
        "open": open_value,
        "close": close_value,
        "high": high_value,
        "low": low_value,
        "volume": volume_value,
        "above_average_count": high_count,
        "below_average_count": low_count,
        "crossover_count": crossover_count,
        "trade_positive": trade_positive,
        "trade_negative": trade_negative,
        "trade_before_crossover": trade_value_before_crossover,
        "trade_after_crossover": trade_value_after_crossover,
    })

    return daywise_results

# Loop to handle fetching data in chunks of up to 100 days
def fetch_and_process_historical_data(total_days=100, step_size=99):
    all_daywise_results = []
    current_time = datetime.now()

    for day_offset in range(0, total_days, step_size):
        end_date = current_time - timedelta(days=day_offset)
        start_date = max(end_date - timedelta(days=step_size), current_time - timedelta(days=total_days))

        start_timestamp = int(start_date.timestamp())
        end_timestamp = int(end_date.timestamp())

        print(f"Fetching data from {start_date} to {end_date}")
        candles = fetch_data(start_timestamp, end_timestamp)

        if candles:
            df_historical_data = pd.DataFrame(
                candles, columns=["date", "open", "high", "low", "close", "volume"]
            )
            daywise_results = process_data(df_historical_data)
            all_daywise_results.extend(daywise_results)

    return all_daywise_results

# Fetch and process data
data = fetch_and_process_historical_data()

# Save results to CSV
df_results = pd.DataFrame(data)
df_results.sort_values(by="date", ascending=False).to_csv("analysis_with_trades.csv", index=False)
























