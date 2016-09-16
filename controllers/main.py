from flask import *
import extensions
main = Blueprint('main', __name__, template_folder='templates')

#initialize database
db=extensions.connect_to_database()
print("db initialized")

@main.route('/')
def main_route():
	cur = db.cursor()
	cur.execute('SELECT username FROM user')
	results = cur.fetchall()
	#first_person_id = results[0]['username']


	options = { 
		"name": 'Damian',
		"users":results,
		"url":url_for('albums.albums_route',username="ytchang"),
	}
	
	return render_template("index.html",**options)