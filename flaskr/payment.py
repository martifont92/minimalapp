from flaskr import app
from flask import request, redirect, url_for, flash
from flask_mail import Mail, Message

import stripe

#Configure mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'martifont92@gmail.com'
app.config['MAIL_PASSWORD'] = 'wkxttnikikkdixrg'

mail = Mail(app)

#Stripe
@app.route('/pay', methods=['POST'])
def pay():

	customer = stripe.Customer.create(
		email=request.form['stripeEmail'],
		source=request.form['stripeToken']
		)
	charge = stripe.Charge.create(
		customer=customer.id,
		amount=int(997),
		currency='eur',
		description='The Product'
		)

	#Sending email after purchase
	msg = Message('Hello', sender = 'martifont92@gmail.com', recipients = [customer.email])
	msg.body = "Testing Flask-email!"
	mail.send(msg)
	#Display success alert
	flash('Payment Successful! We have sent you a download link!')
	return redirect(url_for('shop'))