# files-ms-client-python

Python client for [Node Files Microservice](https://github.com/maxjf1/node-files-microservice)

## Instalation

Install with pip:

```bash
pip3 install git+https://github.com/maxjf1/files-ms-client-python#egg=files-ms-client-python
```

## Usage

For better usage, `FILES_URL` enviroment should be set. 
If not, an `url` argument for the files server URL should be used.

```python
from files_ms_client.client import download, upload, delete

# Upload a file
response = upload('../path/to/file.txt')

# Download a file
download('file_name', '../path/to/new_file.txt')

# Delete a file
delete('file_name')
```
