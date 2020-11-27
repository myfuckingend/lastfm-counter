import time
import json

import requests

BASE_API_LINK = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = '3f8c9de617c17cf1baa38831df0a1eca' # warn! make it secure


def request_one_page_by_username(username):
    params = {
        'username': username,
        'method': 'user.getrecenttracks',
        'api_key': API_KEY,
        'format': 'json',
        'limit': '100',
        'page': '1'
    }
    r = requests.get(BASE_API_LINK, params=params)
    # page = json.loads(data).get('recenttracks').get('track')
    page = json.loads(r.text)
    # page = json.dumps(a, indent=4, ensure_ascii=False)
    print(page)
    return page


username = input('Username: ')
response = request_one_page_by_username(username).get('recenttracks')
total_pages = int(response.get('@attr').get('totalPages'))
prev_track = response.get('track')[0].get('artist').get('#text') + ' - '+ \
             response.get('track')[0].get('name')
print(prev_track)
for page in range(1, total_pages):
    # Print same page ????
    print(page)
    time.sleep(0.25)



