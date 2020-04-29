import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'NXaBykem'
Bootstrap(app)

#Configure SQLite DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/martifont/dev/minimalapp/flaskr/purchase.db'
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    file_name = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)
    price = db.Column(db.Float)

class Purchase(db.Model):
    __tablename__ = 'purchase'
    uuid = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship(Product)
    downloads_left = db.Column(db.Integer, default=5)

#Import views
import flaskr.views

#Import payment
import flaskr.payment


if __name__ == '__main__':
	app.run(debug=True)

