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
import numpy as np

start = datetime.now() - timedelta(days=100) 
start = int(start.timestamp())
end = int(datetime.now().timestamp())

data_requested = {
    "symbol": "NSE:NIFTYBANK-INDEX",
    "resolution": "1",
    "date_format": "0",
    "range_from": start,
    "range_to": end,
    "cont_flag": "1",
}

res = fyers.history(data_requested)

df_historical_data = pd.DataFrame(
    res["candles"], columns=["date", "open", "high", "low", "close", "volume"]
)
df_historical_data["date"] = pd.to_datetime(
    df_historical_data["date"], unit="s", utc=True
).dt.tz_convert("Asia/Kolkata")

df_historical_data.set_index("date", inplace=True)

df_3min = df_historical_data.resample("3T").agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum'
}).dropna()  

df_3min['RSI'] = None
df_3min['ATR'] = None
df_3min['SuperTrend'] = None

def calculate_atr(df, period=14):
    df['H-L'] = df['high'] - df['low']
    df['H-PC'] = abs(df['high'] - df['close'].shift(1))
    df['L-PC'] = abs(df['low'] - df['close'].shift(1))
    df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1)
    df['ATR'] = df['TR'].rolling(window=period, min_periods=1).mean()
    return df.drop(['H-L', 'H-PC', 'L-PC', 'TR'], axis=1)

df_3min = calculate_atr(df_3min)

def calculate_supertrend(df, period=14, multiplier=3, column_name='SuperTrend'):
    df['ATR'] = df['ATR'].rolling(window=period, min_periods=1).mean()
    df[column_name] = np.nan
    df['In_Uptrend'] = True
    df[column_name].iloc[0] = df['close'].iloc[0]
    
    for i in range(1, len(df)):
        current_close = df['close'].iloc[i]
        previous_supertrend = df[column_name].iloc[i-1]
        atr = df['ATR'].iloc[i]
        
        if current_close > previous_supertrend:
            df['In_Uptrend'].iloc[i] = True
        else:
            df['In_Uptrend'].iloc[i] = False
        
        if df['In_Uptrend'].iloc[i]:
            df[column_name].iloc[i] = max(previous_supertrend, current_close - multiplier * atr)
        else:
            df[column_name].iloc[i] = min(previous_supertrend, current_close + multiplier * atr)
    
    return df

df_3min = calculate_supertrend(df_3min, period=7, multiplier=1, column_name='column_1')
df_3min = calculate_supertrend(df_3min, period=10, multiplier=3, column_name='column_2')

def calculate_rsi(df, period=14):
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

df_3min = calculate_rsi(df_3min)

df_3min['crossover'] = 0  
for i in range(len(df_3min)):
    if df_3min['close'][i] > df_3min['column_1'][i] and df_3min['close'][i] > df_3min['column_2'][i]:
        df_3min['crossover'][i] = 1 
    elif df_3min['close'][i] < df_3min['column_1'][i] and df_3min['close'][i] < df_3min['column_2'][i]:
        df_3min['crossover'][i] = -1 
    else:
        df_3min['crossover'][i] = 0  


df_3min['date_only'] = df_3min.index.date    # Add a column for date only for grouping

daily_crossover_counts = df_3min.groupby('date_only')['crossover'].apply(lambda x: (x != 0).sum())  # Count crossovers per day
print(daily_crossover_counts)

df_3min['positive_crossover'] = 0
df_3min['negative_crossover'] = 0

for i in range(len(df_3min)):
    if df_3min['crossover'][i] > 0:
        df_3min['positive_crossover'][i] = df_3min['crossover'][i]  
    elif df_3min['crossover'][i] < 0:
        df_3min['negative_crossover'][i] = df_3min['crossover'][i]  


df_3min.drop(columns=['crossover'], inplace=True)

print(df_3min[['open', 'high', 'low', 'close', 'volume', 'RSI', 'ATR', 'column_1', 'column_2', 'positive_crossover', 'negative_crossover']])



columns_to_exclude = ['volume', 'RSI', 'ATR','SuperTrend','In_Uptrend'] 
df_filtered = df_3min.drop(columns=columns_to_exclude)
df_filtered.to_csv('filtered_data.csv')

