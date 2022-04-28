## Working

2 Sites Exist in this plan:
- Your pages-enabled github repo's site;
- Your Heroku App

### How?
User sends a request to the heroku app like:
	``GET app.herokupp.com/make?src=http://source.com/blogs/me&name=myblog``

The App performs (2 actions):
- Action 1: Whether any other link has taken the name requested (`myblog` here);
	- if yes -> Generate a random name;
	- if no  -> Contnue with the requested name.

- Action 2: Whether the same site (`http://source.com/blogs/me` here) exists in the db:
	- if yes -> Return the site with that name
	- if no  -> Create a new value as `{'myblog':'https://source.com/blogs/me'}`




