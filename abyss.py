import requests
import time
import json


def request_one_page(username):
    params = {
        'username': username,
        'method': 'user.getrecenttracks',
        'api_key': '3f8c9de617c17cf1baa38831df0a1eca',
        'format': 'json',
        'limit': '100',
        'page': '1'
    }
    data = requests.get('http://ws.audioscrobbler.com/2.0/',
                        params=params).text
    # a = json.loads(data).get('recenttracks').get('track')
    a = json.loads(data)
    # a = json.dumps(a, indent=4, ensure_ascii=False)
    print(a)
    return a


username = input('Username: ')
response = request_one_page(username).get('recenttracks')
total_pages = int(response.get('@attr').get('totalPages'))
prev_track = response.get('track')[0].get('artist').get('#text') + ' - '+ \
             response.get('track')[0].get('name')
print(prev_track)
for page in range(1, total_pages):
    print(page)
    time.sleep(0.25)
