#! python3
# download every xkcd comic

import requests, os, bs4

url = 'http://xkcd.com'             # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

while not url.endswith('#'):
    # download page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()




    soup = bs4.BeautifulSoup(res.text)
print('Done.')