from flask import *

from main import db
import os

albums = Blueprint('albums', __name__, template_folder='templates')

@albums.route('/albums/edit',methods=['GET','POST'])
def albums_edit_route():
	options = {
		"edit": True
	}
	cur = db.cursor()
	if request.method=='GET':
		username=request.args['username']		
		cur.execute("SELECT title, albumid, created, lastupdated FROM album WHERE username = %s;", (username,))
		results = cur.fetchall()
		options['albums']=results
		options['username']=username
	elif request.method=='POST':
	
		username=request.form['username']
		if request.form['op']=="delete":
			albumid=request.form['albumid']
			cur.execute("SELECT photo.picid, photo.format FROM photo JOIN contain ON contain.picid=photo.picid WHERE contain.albumid = %s;", (albumid,))
			results = cur.fetchall()
			print(results)
			cur.execute("DELETE FROM contain WHERE albumid= %s",(albumid,))
			for result in results:
				picid=result['picid']
				format=result['format']
				cur.execute("DELETE FROM photo WHERE picid= %s",(picid,))
				os.remove('static/images/'+picid+'.'+format)
			cur.execute("DELETE FROM album WHERE albumid= %s",(albumid,))
			db.commit()
		elif request.form['op']=="add":
			title=request.form['title']
			cur.execute('INSERT INTO album VALUES(NULL, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, %s)',(title,username))
			db.commit()
			
		return redirect( url_for('albums.albums_edit_route',username=username))	
		#return redirect(request.url)		
		
	
	return render_template("albums.html", **options)


@albums.route('/albums',methods=['GET'])
def albums_route():
	
	options = {
		"edit": False
	}
	if request.method == 'GET':
		username=request.args['username']
		cur = db.cursor()
		cur.execute("SELECT title, albumid, created, lastupdated FROM album WHERE username = %s;", (username,))
		results = cur.fetchall()
		options['albums']=results
		options['username']=username
		
	return render_template("albums.html", **options)

	
