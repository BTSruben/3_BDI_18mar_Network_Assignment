#https://github.com/sahildiwan/flask-postgres-heroku
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mypass.1234@db_postgres/postgres'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

# Set "homepage" to index.html
@app.route('/') 
def index():
    users = db.session.query(User).all()
    return render_template('index.html',context={'users':users})

# Save e-mail to database and send to success page
@app.route('/register', methods=['POST'])
def register():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')
