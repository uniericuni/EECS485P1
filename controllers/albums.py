from flask import *

from main import db


albums = Blueprint('albums', __name__, template_folder='templates')

@albums.route('/albums/edit')
def albums_edit_route():
	options = {
		"edit": True
	}
	return render_template("albums.html", **options)


@albums.route('/albums',methods=['GET'])
def albums_route():
	
	options = {
		"edit": False
	}
	if request.method == 'GET':
		username=request.args['username']
		cur = db.cursor()
		cur.execute("SELECT title, albumid FROM album WHERE username = %s;", (username,))
		results = cur.fetchall()
		options['albums']=results
		options['username']=username
		
	return render_template("albums.html", **options)