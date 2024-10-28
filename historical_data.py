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


start = datetime.now() - timedelta(days=4)
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

df_historical_data = pd.DataFrame(res["candles"], columns=["date", "open", "high", "low", "close", "volume"])
df_historical_data["date"] = pd.to_datetime(df_historical_data["date"], unit="s", utc=True).dt.tz_convert("Asia/Kolkata")


start_time = datetime.strptime("09:15", "%H:%M").time()
end_time = datetime.strptime("15:29", "%H:%M").time()

df_historical_data = df_historical_data[(df_historical_data["date"].dt.time >= start_time) & (df_historical_data["date"].dt.time <= end_time)]
df_historical_data = df_historical_data.sort_values(by="date")

df_historical_data['average'] = 0.0
df_historical_data['higher']= 0
df_historical_data['lower']= 0
day=None



day = date(1001, 12, 12)

for i in range(len(df_historical_data)):
        current_date = df_historical_data["date"][i].strftime("%Y-%m-%d")
        current_time = df_historical_data["date"][i].time()
        if current_time == start_time:
            day = current_date
        elif current_date == day and start_time <= current_time <= end_time:
            pass
        else:
            continue

for i in range(len(df_historical_data)):
    if day != df_historical_data["date"][i].strftime("%Y-%m-%d"):
        day = df_historical_data["date"][i].strftime("%Y-%m-%d")
        
        high=df_historical_data["high"][i]
        low=df_historical_data["low"][i]
        df_historical_data['average'][i] = (high + low) / 2  
        average = (high + low) / 2

    else:
        
        df_historical_data['average'][i] = average  
        if df_historical_data["close"][i] >= average:
            df_historical_data['higher'][i] = 1 
        elif df_historical_data["close"][i] <= average:
            df_historical_data['lower'][i] = 1
        else:
            break

print(df_historical_data)

df_historical_data.to_csv("historical_data_output.csv")
















































































































































