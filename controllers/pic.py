from flask import *

pic = Blueprint('pic', __name__, template_folder='templates',url_prefix='/24b8g606/p1')

@pic.route('/pic')
def pic_route():
	return render_template("pic.html")