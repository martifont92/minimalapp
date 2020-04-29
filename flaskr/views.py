from flaskr import app
from flask import render_template

import stripe

#Stripe
pub_key = 'pk_test_T7FKDbqcVOQByT6Cl6YBgPFj00y52ZO2hb'
secret_key = 'sk_test_uLduAGXEEL228gykOuUPktgu00sQrbP8KM'
stripe.api_key = secret_key

#Views
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/shop')
def shop():
	return render_template('shop.html', pub_key= pub_key)