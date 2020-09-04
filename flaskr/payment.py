from flaskr import app
from flask import request, redirect, url_for, flash, Blueprint
from flask_mail import Mail, Message

#Stripe
import stripe
pub_key = 'pk_test_T7FKDbqcVOQByT6Cl6YBgPFj00y52ZO2hb'
secret_key = 'sk_test_uLduAGXEEL228gykOuUPktgu00sQrbP8KM'
stripe.api_key = secret_key

app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_T7FKDbqcVOQByT6Cl6YBgPFj00y52ZO2hb'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_uLduAGXEEL228gykOuUPktgu00sQrbP8KM'

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
	flash('Payment Successful! Thank you for your purchase!')
	return redirect(url_for('main.shop'))