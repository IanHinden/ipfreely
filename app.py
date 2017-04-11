from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/ipfree'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class IP(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ip_address = db.Column(db.String, unique=True)
	free = db.Column(db.Boolean)

	def __init__(self, ip_address, free):
		self.ip_address = ip_address
		self.free = free

	def __repr__(self):
		return '<IP %r>' % self.ip_address

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()