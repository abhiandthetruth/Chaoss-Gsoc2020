import perceval.backends.core.github as github
import perceval.backends.core.gitlab as gitlab
from configparser import ConfigParser

"""Getting the configuration"""
config = ConfigParser()
config.read('config.ini')

"""Github Section"""

# Specifying Owner of Repositories
owner = 'abhiandthetruth'

# Specifying name of the repository
repository = 'perceval-voice'

# Getting the key
api_keys= [config.get('ApiKeys', 'github_key')]

# Creating the object
repo = github.GitHub(owner=owner, repository=repository, api_token=api_keys)

# Getting list of issues and prs
issueList = repo.fetch(category='issue')
prList = repo.fetch(category='pull_request')

# printing the issues
for issue in issueList:
    print(issue)

"""GitLab Section"""

# Specifying Owner of Repositories
owner = 'pgjones'

# Specifying name of the repository
repository = 'quart'

# Getting the key
api_keys = config.get('ApiKeys', 'gitlab_key')

# Creating the object of the repository
repo = gitlab.GitLab(owner=owner, repository=repository, api_token=api_keys)

# Getting list of issues and prs
issueList = repo.fetch(category='issue')
prList = repo.fetch(category='pull_request')

# printing the issues
for issue in issueList:
    print(issue)
