from flask import *
from main import db

pic = Blueprint('pic', __name__, template_folder='templates',url_prefix='/24b8g606/p1')

@pic.route('/pic',methods=['GET'])
def pic_route():	
	options={
		"prev_pic": False,
		"next_pic": False
	}
	picid=request.args['picid']
	cur = db.cursor()
	cur.execute("SELECT photo.picid, photo.format, contain.albumid FROM photo JOIN contain ON contain.picid=photo.picid WHERE photo.picid = %s;", (picid,))
	results = cur.fetchone()
	options['picture']=results
	options['picture']['route']='images/'+picid+'.'+results['format']
	options['albumid']=results['albumid']
	options['picid']=picid
	
	cur.execute("SELECT contain.picid, contain.sequencenum FROM contain WHERE contain.albumid = %s ORDER BY contain.sequencenum;", (options['albumid'],))
	results = cur.fetchall()
	for i, result in enumerate(results):
		if(result['picid'] == picid):
			index = i;
	if(index>0):
		options['prev_pic']=True
		options['prev_picid']=results[index-1]['picid']
	if(index<len(results)-1):
		options['next_pic']=True
		options['next_picid']=results[index+1]['picid']
	return render_template("pic.html", **options)
