import perceval.backends.core.github as github
import perceval.backends.core.gitlab as gitlab

from configparser import ConfigParser


"""Getting the configuration"""

config = ConfigParser()
config.read('config.ini')


"""Github Section"""

# Getting the repos
repos = config.get('Github', 'repos').split(',')

# Getting the key
api_keys = [config.get('Github', 'key')]

if '' not in repos:
    for repo in repos:
        owner = repo.split('/')[0].strip()
        repository = repo.split('/')[1].strip()
        print(owner, repository)
        # Creating the object
        repo = github.GitHub(owner=owner, repository=repository, api_token=api_keys)
        # Getting list of issues and prs
        issueList = repo.fetch(category='issue')
        prList = repo.fetch(category='pull_request')
        # printing the issues
        for issue in issueList:
            print(issue)


"""Gitlab Section"""

# Getting the repos
repos = config.get('Gitlab', 'repos').split(',')

# Getting the key
api_keys = config.get('Gitlab', 'key')

if '' not in repos:
    for repo in repos:
        owner = repo.split('/')[0].strip()
        repository = repo.split('/')[1].strip()
        print(owner, repository)
        # Creating the object of the repository
        repo = gitlab.GitLab(owner=owner, repository=repository, api_token=api_keys)
        # Getting list of issues and prs
        issueList = repo.fetch(category='issue')
        prList = repo.fetch(category='pull_request')
        # printing the issues
        for issue in issueList:
            print(issue)

