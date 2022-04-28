import flask
import ShitDB
from flask import request as req
import utils


app = flask.Flask(__name__)
db = ShitDB.DB(utils.constant("github_token"), utils.constant("repo"), utils.constant("creds"))
utils.db=db


@app.route("/")
def index():
	return flask.render_template("index.html") # OR utils.pages("index.html")

@app.route("/make")
def make():
	src = req.args.get("src")
	name = req.args.get("name")

	if not src:
		return {'error':True, 'msg':'"src" is a required param.', 'code':403}, 403
	if utils.link_exists(src) is False:
		return {'error':True, 'msg':f'{src} could not be found.','code':401}, 401

	name = utils.check_and_assign_name(name,src) # if None, returns random name

	db.push_remote_data(utils.create_redirect_code(src),f"{name}.html", msg=f"{src} Added")

	return {'src':src,'redirect':f'{utils.constant("host_url")}/{name}','error':False,'code':200}, 200


# Add endpoints explictly!
app.add_url_rule("/index",index)


if __name__=="__main__":
	app.run("0.0.0.0") # fr

