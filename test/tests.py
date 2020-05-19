import sys, os.path
modules_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+ '/src/files_ms_client/')
sys.path.append(modules_dir)

# Usage example
from client import download, upload, delete
url = 'http://localhost:3000'
r = upload('../temp/test.jpg', url)
print(r)
download(r['name'], '../temp/result.jpg', url)
print(
    delete(r['name'], url)
)