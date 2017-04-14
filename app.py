from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from IP_Status import *

@app.route('/')
def index():
	addresses = IpStatus.query.all()
	return render_template('index.html', addresses = addresses)

@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
	id = IpStatus.query.get(id)
	id.free = False
	db.session.commit()

	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run()