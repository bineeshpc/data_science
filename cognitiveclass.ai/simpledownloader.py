import requests
import os

def download(url_, filename):
    if not os.path.exists(filename):
        r = requests.get(url_, allow_redirects=True, verify=False)
        with open(filename, 'wb') as f:
            f.write(r.content)
    else:
        print(f"{filename} already exists")
