import requests

CLIENT_ID = '_5kJYHl821g7qUal3YTyYQ'
SECRET_TOKEN = '98kM-SMeH_RRhlYAiKMV35doOTbNXw'

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'InternationalOwl790',
        'password': 'tempredditaccount'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'covid_vax/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

api_url = 'https://oauth.reddit.com'

# while the token is valid (~2 hours) we just add headers=headers to our requests
response = requests.get(api_url + '/api/v1/me', headers=headers)

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])

payload = {'q': 'vaccine', 'limit': 5, 'sort': 'relevance'}
response = requests.get(api_url + '/subreddits/search', headers=headers, params=payload)
print(response.json())