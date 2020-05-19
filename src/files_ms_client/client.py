from os import getenv
from requests import post, get
import json

files_url = (getenv('FILES_URL') or '')
file_key = 'file'


def upload(file: str, url: str = files_url):
    # Upload a file to the server
    files = {file_key: open(file, 'rb')}
    r = post(f'{url}/files', files=files)
    return r.json()[file_key]


def download(file: str, path: str, url: str = files_url):
    # Download a file from the server
    r = get(f'{url}/files/{file}')
    open(path, 'wb').write(r.content)
