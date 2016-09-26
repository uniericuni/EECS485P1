from flask import *
from main import db
import os
import hashlib

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'bmp', 'gif','PNG', 'JPG', 'BMP', 'GIF'])
IMAGE_FOLDER='static/images/'

album = Blueprint('album', __name__, template_folder='templates',url_prefix='/24b8g606/p1')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@album.route('/album/edit',methods=['GET','POST'])
def album_edit_route():
	options = {
		"edit": True
	}
	cur = db.cursor()
	if request.method == 'GET':
		if 'albumid' not in request.args:
			abort(404)
		albumid=request.args['albumid']	
		cur.execute("SELECT albumid FROM album WHERE albumid= %s;",(albumid,))
		if(len(cur.fetchall())==0):
			abort(404)	
			
		cur.execute("SELECT photo.picid, photo.format FROM photo JOIN contain ON contain.picid=photo.picid WHERE contain.albumid = %s ORDER BY contain.sequencenum;", (albumid,))
		results = cur.fetchall()
		options['pictures']=results
		options['albumid']=albumid
		for picture in options['pictures']:
			picture['route']='images/'+picture['picid']+'.'+picture['format']
	elif request.method=='POST':
		albumid=request.form['albumid']
		if request.form['op']=="delete":
			picid=request.form['picid']
			cur.execute("SELECT format FROM photo WHERE picid = %s;", (picid,))
			results = cur.fetchone()
			format=results['format']
			#print(results)
			cur.execute("DELETE FROM contain WHERE picid= %s",(picid,))
			cur.execute("DELETE FROM photo WHERE picid= %s",(picid,))
			os.remove(IMAGE_FOLDER+picid+'.'+format)
			
			#update timestamp
			cur.execute('UPDATE album SET lastupdated=CURRENT_TIMESTAMP WHERE albumid=%s;',(albumid,))
			
			db.commit()

			return redirect(url_for('album.album_edit_route',albumid=albumid))
		elif request.form['op']=="add":
			# check if the post request has the file part
			if 'file' not in request.files:
				flash('No file part')
				return redirect(url_for('album.album_edit_route',albumid=albumid))
			file = request.files['file']
			# if user does not select file, browser also
			# submit a empty part without filename
			if file.filename == '':
				flash('No selected file')
				return redirect(url_for('album.album_edit_route',albumid=albumid))
			
			filename=file.filename
			if file and allowed_file(filename):
				#make hash
				htable = hashlib.md5()
				dotNum = filename.find('.')
				fname = filename[0:len(filename)]
				fformat = filename[dotNum+1:len(filename)]
				htable.update(str(albumid))
				htable.update(filename)
				picid = htable.hexdigest()
				
				#get proper sequence number for contain
				cur.execute("SELECT sequencenum FROM contain;")
				results=cur.fetchall()
				nums=[item['sequencenum'] for item in results]
				num=max(nums)+1
				#save to database
				cur.execute("INSERT INTO photo VALUES( %s, %s, CURRENT_TIMESTAMP);",(fformat,str(picid)))
				cur.execute("INSERT INTO contain VALUES( %s, %s, %s, '');",(num,albumid,picid))
				
				#update timestamp
				cur.execute('UPDATE album SET lastupdated=CURRENT_TIMESTAMP WHERE albumid=%s;',(albumid,))
				
				#save to folder
				filename = secure_filename(picid+'.'+fformat)
				file.save(IMAGE_FOLDER+filename)
				db.commit()
			return redirect(url_for('album.album_edit_route',albumid=albumid))
				#file=
	return render_template("album.html", **options)

@album.route('/album',methods=['GET'])
def album_route():
	options = {
		"edit": False
	}
	if request.method == 'GET':
		if 'albumid' not in request.args:
			abort(404)
		albumid=request.args['albumid']
		cur = db.cursor()
		cur.execute("SELECT albumid FROM album WHERE albumid= %s;",(albumid,))
		if(len(cur.fetchall())==0):
			abort(404)		
		
		cur.execute("SELECT photo.picid, photo.format, contain.sequencenum FROM photo JOIN contain ON contain.picid=photo.picid WHERE contain.albumid = %s ORDER BY contain.sequencenum;", (albumid,))
		results = cur.fetchall()
		options['pictures']=results
		options['albumid']=albumid
		for picture in options['pictures']:
			picture['route']='images/'+picture['picid']+'.'+picture['format']
		
	return render_template("album.html", **options)
