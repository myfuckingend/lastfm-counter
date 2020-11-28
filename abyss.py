import time
import json
from collections import Counter

import requests

BASE_API_LINK = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = '3f8c9de617c17cf1baa38831df0a1eca' # warn! make it secure


def get_recenttracks(username, page_number):
    params = {
        'username': username,
        'method': 'user.getrecenttracks',
        'api_key': API_KEY,
        'format': 'json',
        'limit': '1000',
        'page': page_number
    }
    r = requests.get(BASE_API_LINK, params=params)
    return json.loads(r.text).get('recenttracks')


username = input('Username: ')
response = get_recenttracks(username, 1)
total_pages = int(response.get('@attr').get('totalPages'))
prev_track = response.get('track')[0].get('artist').get('#text') + ' - ' + \
             response.get('track')[0].get('name')
print('Most recent track:', prev_track)
print('Total pages to parse:', total_pages)
counter = Counter()
a = 0
for page in range(1, total_pages+1):
    current_page = get_recenttracks(username, page).get('track')
    print('Current page:', page)
    for track in current_page:
        if track.get('@attr'):
            print('Please close your music player')
        else:
            curr_track = track.get('artist').get('#text') + ' - ' + \
                         track.get('name')
            if prev_track != curr_track:
                prev_track = curr_track
                a = 0
                if counter[curr_track]:
                    while True:
                        a += 1
                        if counter[curr_track + ' (another portion ' + str(a) + ')']:
                            pass
                        else:
                            break
            if a == 0:
                counter[curr_track] += 1
            else:
                counter[curr_track + ' (another portion ' + str(a) + ')'] += 1
    time.sleep(0.25)

for title, count in counter.most_common(20):
    print(title + ': ' + str(count))
