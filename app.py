from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from IP_Status import *

@app.route('/')
def index():
	addresses = IpStatus.query.all()
	return render_template('index.html', addresses = addresses)

if __name__ == "__main__":
	app.run()