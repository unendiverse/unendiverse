# Profile README.md Updater
# For use with GitHub Actions

from github import Github
import os

readme = open('README.md', 'w')
githubapi = Github(os.environ.get('GITHUB_TOKEN'))

readme.write('Repos:\n')
for repo in githubapi.get_user().get_repos(visibility='public'):
    readme.write(repo + '\n')
