from github import Github
from git import Repo
from pathlib import Path
import os


if not os.environ["github_token"]:
    print("ERROR: You need to specify the github_token as environment variable!")
    exit(1)

token = os.environ["github_token"]

g = Github(token)

path = Path("/backup/")

username = g.get_user().login

for repo in g.get_user().get_repos():
    print(repo.name)
    c_path = path / repo.name
    if not c_path.exists() or not c_path.is_dir():
        c_path.mkdir(parents=True)
    git_path = c_path / ".git"
    if git_path.exists():
        r = Repo(c_path)
        for remote in r.remotes:
            fetchinfo = remote.fetch()
            for f in fetchinfo:
                print("Fetch:", f)
            pullinfo = remote.pull()
            for p in pullinfo:
                print("Pull:", p)
    else:
        url = repo.clone_url
        print("Clone:", url)
        clone_url = url[:8] + username + ":" + token + "@" + url[8:]
        #print(clone_url)
        Repo.clone_from(clone_url, c_path)
    
