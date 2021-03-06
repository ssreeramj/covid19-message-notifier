import requests
import json

from get_message import short_message
from credentials import API_KEY, SECRET_KEY

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype': useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
mobile_number = '' # Enter 10 digit mobile number
response = sendPostRequest(URL, API_KEY, SECRET_KEY, 'stage', mobile_number, 'SMSIND', short_message)

# print response if you want
print(response.text)
