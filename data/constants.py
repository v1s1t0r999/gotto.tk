import os

_dict = {
'github_token' : os.getenv("GTK"),  # https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
'repo' : os.getenv("REPO"), # name of the repo which is to be used as the site base
'creds' : (os.getenv("USERNAME"),os.getenv("EMAIL")), # ("github_username", "github_conneted_email")
'host_url': os.getenv("HOST_URL"), # the github pages site name OR the CNAME if you are connecting to any other domain
'branch':os.getenv("BRANCH") # The github pages branch
}
