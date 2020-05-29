import sys, os.path
modules_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+ '/src/')
sys.path.append(modules_dir)

from os import getenv
url = getenv('FILES_URL', 'http://localhost:3000')

# Usage example
from files_ms_client import download, upload, delete
url = 'http://localhost:3000'
r = upload('../temp/test.jpg', url=url)
print(r)
download(r['name'], '../temp/result.jpg', url=url)
print(
    delete(r['name'], url=url)
)