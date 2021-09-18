import requests
import os
from dotenv import find_dotenv, load_dotenv


client_ID = os.getenv('client_id')
client_secret=os.getenv('client_secret')
access_token = 'BQBwKFM4qgAhintiaaGvNLKo1FFzLpO-nuaRcRemaEeO41Nvd08aaePDUUFaKRLE5MSCEuXJI8ZxQSW5MV_sPE5Bc532TwB_Hg78YBZB0NLR3BJOp5PI063cLfsK-RvoH7ofwOiPxNvzoA'
AUTH_URL = "https://accounts.spotify.com/api/token"

response = requests.get("https://api.spotify.com/v1/browse/new-releases")
response_json = response.json()

auth_response = requests.post(AUTH_URL, {
    'grant_type' : 'client_credentials',
    'client_id' : client_ID,
    'client_secret' : client_secret,
   
})

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

print(response.json())

