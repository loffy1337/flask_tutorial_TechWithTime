from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'simple-secret-key'
app.permanent_seesion_lifetime = timedelta(minutes=1)


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/login', methods=['GET', 'POST',])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		session.permanent = True
		session['user'] = user
		return redirect(url_for('user'))
	if 'user' in session:
		return redirect(url_for('user'))
	return render_template('login.html')


@app.route('/logout')
def logout():
	session.pop('user', None)
	return redirect(url_for('login'))


@app.route('/user')
def user():
	if 'user' in session:
		user = session['user']
		return f'<h1>{user}</h1>'
	return redirect(url_for('login'))


if __name__ == '__main__':
	app.run(debug=True)
