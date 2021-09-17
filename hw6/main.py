import requests
import os 
from dotenv import find_dotenv,load_dotenv


load_dotenv(find_dotenv())


client_id = os.getenv('client_id')
client_secret=os.getenv('client_secret')

redirect_uri = 'hw6-swe-bseddiqi1://callback/'
#access_token = 'BQDREXdVx-Ox1fxvqoWoGJIIfdqaePOL3Fyc5tc8qb-NHGMh1qWZlbcLYDbEGo47ObuyxE7g8Ry04c7mGgMoK3v3_9K13j0RXLPXylnLx1zLkBt7kuFuIVOT4obmVIdMUPuHWmnIWWQNQQ'

AUTH_URL = 'https://accounts.spotify.com/api/token'

#POST?
auth_response = requests.post(AUTH_URL, {
    'grant_type' : 'client_credentials',
    'client_id' : client_id,
    'client_secret' : client_secret,
    #'redirect_uri' : redirect_uri
})

#convert response to json
auth_response_data = auth_response.json()

#save access token 
#ticket to access API
access_token=auth_response_data['access_token']
#for authentication or metadata for request 
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/browse/new-releases'

r = requests.get (f"https://api.spotify.com/v1/browse/new-releases?country=SE&offset=0&limit=20", headers=headers) 
r = r.json()

for i in range (10):
    print(r['albums']['items'][i]['name'])