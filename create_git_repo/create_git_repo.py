import os
import sys
from dotenv import load_dotenv
from github import Github

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("GIT_USER")
password = os.getenv("GIT_PASSWORD")

def create_repo():

    repo_folder_name = str(sys.argv[1])
    repo_already_exists = os.path.exists(path + repo_folder_name)

    if repo_already_exists:
        print(f'{repo_folder_name} repo already exists. Please chose another name.')
    else:
        os.makedirs(path + repo_folder_name)
        user = Github(username, password).get_user()
        repo = user.create_repo(repo_folder_name)
        print(f'Successfully created repository: {repo_folder_name}')
    
if __name__ == "__main__":
    create_repo()