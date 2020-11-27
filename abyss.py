import time
import json

import requests

BASE_API_LINK = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = '3f8c9de617c17cf1baa38831df0a1eca' # warn! make it secure


def request_one_page(username, page_number):
    params = {
        'username': username,
        'method': 'user.getrecenttracks',
        'api_key': API_KEY,
        'format': 'json',
        'limit': '100',
        'page': page_number
    }
    r = requests.get(BASE_API_LINK, params=params)
    data = json.loads(r.text).get('recenttracks')
    # page = json.dumps(a, indent=4, ensure_ascii=False)
    print(data)
    return data


username = input('Username: ')
response = request_one_page(username, 1)
total_pages = int(response.get('@attr').get('totalPages'))
prev_track = response.get('track')[0].get('artist').get('#text') + ' - ' + \
             response.get('track')[0].get('name')
print('Most recent track:', prev_track)
print('Total pages to parse:', total_pages)
for page in range(1, total_pages+1):
    current_page = request_one_page(username, page).get('track')
    print('Current page:', page)
    # for track in current_page:
    #     print('some parsing')
    time.sleep(0.25)
