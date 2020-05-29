"""
# Files Microservice Client

Python client for Node Files Microservice (https://github.com/maxjf1/node-files-microservice)

By default, `FILES_URL` enviroment variable is used to access the 
files server, but it can be overriden by the `url` argument in all methods.
"""

from os import getenv, remove
import requests as req
import json
from mimetypes import guess_type

files_url = getenv('FILES_URL', '')
file_key = 'file'

def upload(file: str, delete: bool = False, url: str = files_url, buffer: bool = False, mime: str = None):
    """Upload a file to the server
    
    Can be passed an file path or a buffer, but if an buffer is passed, 
    the `buffer` argument must be `true` and a `mime` type should be passed too.
    
    If `delete` is true, the file will be deleted after upload"""
    if not buffer:
        mime = guess_type(file)[0]
        file = open(file, 'rb')

    files = {file_key: ('file', file, mime)}
    r = req.post(f'{url}/files', files=files)
    if delete:  # Delete the file
        remove(file)
    return r.json()[file_key]


def download(file: str, path: str = None, url: str = files_url, buffer: bool = False):
    """Download a file from the server
    
    if `buffer` is `true`, it will return the file buffer"""
    r = req.get(f'{url}/files/{file}')
    if(buffer):
        return r.content
    open(path, 'wb').write(r.content)


def delete(file: str, url: str = files_url):
    """Delete a file from the server"""
    r = req.delete(f'{url}/files/{file}')
    return r.json()