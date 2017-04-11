from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import IP_Status

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/ipfree'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()