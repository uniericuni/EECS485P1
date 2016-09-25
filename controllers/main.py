from flask import *
import extensions
main = Blueprint('main', __name__, template_folder='templates',url_prefix='/24b8g606/p1')

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
		"users":results,
	}
	
	return render_template("index.html",**options)