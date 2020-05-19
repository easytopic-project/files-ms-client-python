from os import getenv
from requests import post, get
import json

files_url = (getenv('FILES_URL') or '')
file_key = 'file'

# Upload a file to the server
def upload(file: str, url: str = files_url):
    files = {file_key: open(file, 'rb')}
    r = post(f'{url}/files', files=files)
    return r.json()[file_key]

# Download a file from the server
def download(file: str, path: str, url: str = files_url):
    
    r = get(f'{url}/files/{file}')
    open(path, 'wb').write(r.content)
