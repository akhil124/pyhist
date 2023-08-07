import requests
import json

def get_commit_history(username, repo):
    url = f'https://api.github.com/repos/{username}/{repo}/commits'
    response = requests.get(url)
    
    if response.status_code != 200:
        # An error occured
        raise Exception(f'Request failed with status {response.status_code}')
    
    commit_data = response.json()
    
    # Print commit details
    for commit in commit_data:
        print(f'Commit SHA: {commit["sha"]}')
        print(f'Author: {commit["commit"]["author"]["name"]}')
        print(f'Date: {commit["commit"]["author"]["date"]}')
        print(f'Message: {commit["commit"]["message"]}')
        print('------')

# Replace 'your-username' and 'your-repo' with the real username and repo name
get_commit_history('akhil124', 'Image-Search')
