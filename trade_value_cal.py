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


from datetime import datetime, timedelta
import pandas as pd
import pytz

# Define start and end times (last 4 days)
start = datetime.now() - timedelta(days=4)
start = int(start.timestamp())
end = int(datetime.now().timestamp())

# Data request payload
data_requested = {
    "symbol": "NSE:NIFTYBANK-INDEX",
    "resolution": "1",
    "date_format": "0",
    "range_from": start,
    "range_to": end,
    "cont_flag": "1",
}

# Fetch historical data
res = fyers.history(data_requested)

# Create a DataFrame
df_historical_data = pd.DataFrame(res["candles"], columns=["date", "open", "high", "low", "close", "volume"])

df_historical_data["date"] = pd.to_datetime(df_historical_data["date"], unit="s", utc=True).dt.tz_convert("Asia/Kolkata")


start_time = datetime.strptime("09:15", "%H:%M").time()
end_time = datetime.strptime("15:29", "%H:%M").time()

df_historical_data = df_historical_data[
    (df_historical_data["date"].dt.time >= start_time) &
    (df_historical_data["date"].dt.time <= end_time)
]

df_historical_data["avg"] = ((df_historical_data["high"] + df_historical_data["low"]) / 2).astype(int)

df_historical_data["crossover"] = (df_historical_data["close"] > df_historical_data["avg"]).astype(int)

# Trade value (close - average)
df_historical_data["trade_value"] = (df_historical_data["close"] - df_historical_data["avg"]).astype(int)

print(df_historical_data[["date", "open", "high", "low", "close", "avg", "crossover", "trade_value"]])


df_historical_data.to_csv("historical_data_output.csv")


















# from datetime import datetime, timedelta
# import pandas as pd
# import pytz

# # Assuming fyers is defined and authenticated elsewhere
# start = datetime.now() - timedelta(days=5)
# start = int(start.timestamp())
# end = int(datetime.now().timestamp())

# # Data for fyers API call
# data = {
#     "symbol": "NSE:NIFTYBANK-INDEX",
#     "resolution": "1",
#     "date_format": "0",
#     "range_from": start,
#     "range_to": end,
#     "cont_flag": "1",
# }

# # Call the Fyers API and convert the response data to a DataFrame
# res = fyers.history(data)
# data = pd.DataFrame(
#     res["candles"], columns=["date", "open", "high", "low", "close", "volume"]
# )

# # Convert the timestamp to proper datetime format
# data["date"] = pd.to_datetime(data["date"], unit="s").dt.tz_localize("UTC").dt.tz_convert("Asia/Kolkata")

# # Filter data between 09:15 and 15:29
# start_time = datetime.strptime("09:15", "%H:%M").time()
# end_time = datetime.strptime("15:29", "%H:%M").time()
# data = data[(data["date"].dt.time >= start_time) & (data["date"].dt.time <= end_time)]

# # Add a column to store the average of high and low
# data["average"] = (data["high"] + data["low"]) / 2

# # Initialize trade value columns
# data["trade_1"] = 0
# data["trade_2"] = 0
# data["trade_3"] = 0

# # Initialize variables for trade tracking
# active_trade = 1  # Track which trade segment is active
# trade_value = 0  # Counter for trade value

# # Function to calculate trade values based on crossovers
# def calculate_trade_values(data):
#     global active_trade, trade_value
    
#     for i in range(1, len(data)):
#         close_current = data["close"].iloc[i]
#         close_prev = data["close"].iloc[i - 1]
#         avg_current = data["average"].iloc[i]
#         avg_prev = data["average"].iloc[i - 1]

#         # Detect upward crossover
#         if close_current > avg_current and close_prev <= avg_prev:
#             if active_trade == 1:
#                 data.at[i, "trade_1"] = trade_value
#             active_trade = 2

#         # Detect downward crossover
#         elif close_current < avg_current and close_prev >= avg_prev:
#             if active_trade == 2:
#                 data.at[i, "trade_2"] = trade_value
#             active_trade = 3

#         # Accumulate trade values
#         trade_value += 1
#         if active_trade == 1:
#             data.at[i, "trade_1"] = trade_value
#         elif active_trade == 2:
#             data.at[i, "trade_2"] = trade_value
#         elif active_trade == 3:
#             data.at[i, "trade_3"] = trade_value

#     return data

# # Apply the function to calculate trade values
# data = calculate_trade_values(data)

# # Select relevant columns for output
# result = data[["date", "close", "trade_1", "trade_2", "trade_3"]]

# # Output the result
# print(result)

# # Save the result to a CSV file
# result.to_csv("trade_values_result33.csv2", index=False)
