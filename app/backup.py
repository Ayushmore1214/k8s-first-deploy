import requests, zipfile, io
from google.cloud import storage
import os

def backup_repo(username, repo, token):
    headers = {'Authorization': f'token {token}'}
    url = f"https://api.github.com/repos/{username}/{repo}/zipball"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        bucket_name = os.environ.get("GCS_BUCKET_NAME")
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(f"{username}/{repo}.zip")
        blob.upload_from_string(response.content)
        return blob.public_url
    return None
