# Friday April 07, 2022
# 4:28 PM
# v1s1t0r999 (Sorta Lost)


# {"strange-wtf-nou":"source.com/blog/urmomlol"}

import errors
import secrets
import requests as r
import random
import flask


global db
db = None



redirect_quotes = ["redirecting","omw","on it..","a sec bro","pls wait or go kys","heh..NO","bruhv wait!",":|","-_-","u can't go more lame duh"]




def gen_random_words(wordlist="data/words.txt"):
	with open(wordlist,"r") as f:
		con = f.read() # "w1\nw2\nw3\nw4"
	lst = con.rsplit("\n") # ["w1","w2","w3","w4"]
	namelst=[]
	for i in range(1,random.choice([2,3,4])):
		namelst.append(random.choice(lst)) # ["w3","w1"]
	name="-".join(namelst) # "w3-w1"
	return name



def constant(c):
	from data import constants
	try:
		return constants._dict[c.lower()]
	except KeyError:
		raise errors.IncorrectVal(f"{c} is invalid!")


def _endpoint(ep,data):
	try:
		data[ep.lower()]
		return True     # "ep" name exists in db! Returns the redirect-site
	except KeyError:
		return False  # "ep" doesn't exists so generate a random_word

def _src(src,data):
	for elem in data:
		if data[elem.lower()].lower()==src.lower():
			return data[elem.lower()].lower(), True
	return "nu",False



def check_and_assign_name(name,src):
	"""
	DAMN
	"""
	name=name.lower()
	if name is None:
		name = gen_random_words()
	all_links = db.load_remote_data("all_links.json",eval_output=True)

	if _endpoint(name,all_links) is True: # already in db!
		name = gen_random_words() # gen smth else!

	src_chk = _src(src,all_links)
	if src_chk[1] is True:
		return src_chk[0]


	all_links.update({name:src.lower()})
	db.push_remote_data(all_links,"all_links.json",msg=f"{src} Added")
	return name




def create_redirect_code(src):
	"""
	Creates the basic redirective html code for a given link.
	Just `flask.redirect(src)` also works lmaoo
	"""
	return flask.render_template("redirect.html",title=random.choice(redirect_quotes),src=src)




def pages(page):
	"""
	Returns the content of any file in data dir. File should exist.
	"""
	with open(f"data/{page.lower()}","r") as f:
		con = f.read()
	return con




def link_exists(src):
	try:
		site = r.get(src,timeout=2)
	except r.ConnectionError:
		return False
	if site.status_code==404:
		return False
	return True








