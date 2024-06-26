from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'simple-secret-key'
app.permanent_seesion_lifetime = timedelta(minutes=5)


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/login', methods=['GET', 'POST',])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		session.permanent = True
		session['user'] = user
		flash('Login succesful!')
		return redirect(url_for('user'))
	if 'user' in session:
		flash('Already logged in!!')
		return redirect(url_for('user'))
	return render_template('login.html')


@app.route('/logout')
def logout():
	if 'user' in session:
		user = session['user']
		flash(f'You have been logged out, {user}!', 'info')
	session.pop('user', None)
	return redirect(url_for('login'))


@app.route('/user')
def user():
	if 'user' in session:
		user = session['user']
		return render_template('user.html', user=user)
	flash('You are not logged in!')
	return redirect(url_for('login'))


if __name__ == '__main__':
	app.run(debug=True)
