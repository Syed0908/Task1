from github import Github
import credential
g = Github(credential.access_token)
user = g.get_user()
repo = user.get_repo("Task1")
file = repo.get_contents("")
count=0
for content in file:
    count+=1
    print(f"File number {count} is {content.path}")
    print(content.path)
    print(content.decoded_content.decode())