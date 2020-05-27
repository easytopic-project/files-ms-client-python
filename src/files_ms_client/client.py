from os import getenv, remove
import requests as req
import json
from mimetypes import guess_type

files_url = getenv('FILES_URL', '')
file_key = 'file'


def upload(file: str, delete: bool = False, url: str = files_url):
    """Upload a file to the server"""
    files = {file_key: (file, open(file, 'rb'), guess_type(file)[0])}
    r = req.post(f'{url}/files', files=files)
    if delete:  # Delete the file
        remove(file)
    return r.json()[file_key]


def download(file: str, path: str, url: str = files_url):
    """Download a file from the server"""
    r = req.get(f'{url}/files/{file}')
    open(path, 'wb').write(r.content)


def delete(file: str, url: str = files_url):
    """Delete a file from the server"""
    r = req.delete(f'{url}/files/{file}')
    return r.json()
