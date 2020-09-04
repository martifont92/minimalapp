#from flaskr import app
from flask import render_template, Blueprint

import stripe
pub_key = 'pk_test_T7FKDbqcVOQByT6Cl6YBgPFj00y52ZO2hb'
secret_key = 'sk_test_uLduAGXEEL228gykOuUPktgu00sQrbP8KM'
stripe.api_key = secret_key

main = Blueprint('main', __name__, url_prefix="", static_folder="static", template_folder="templates")

#Views
@main.route('/')
def index():
	return render_template('index.html')

@main.route('/about')
def about():
	return render_template('about.html')

@main.route('/contact')
def contact():
	return render_template('contact.html')

@main.route('/shop')
def shop():
	return render_template('shop.html', pub_key = pub_key) 