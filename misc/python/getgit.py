from github import Github
from github import GithubException
import os

Token = os.getenv('GithubToken')
TargetOrg = os.getenv('TargetOrg')
g = Github(Token)

for repo in g.get_organization(TargetOrg).get_repos():
    print(repo.name)