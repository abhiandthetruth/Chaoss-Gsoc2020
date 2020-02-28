from perceval.backends.core.git import Git

url = 'http://github.com/abhiandthetruth/JournalJar'

dir = './temp/Saarthi'

repo = Git(uri=url, gitpath=dir)

for commit in repo.fetch():
    print(commit)