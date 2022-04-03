from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
from flask_login import currents_user, login_user, logout_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Javier'}
	posts = [
		{
			'author': {'username': 'Jenn'},
			'body': 'Maestra de ingles.'
		},
		{
			'author': {'username': 'Diana'},
			'body': 'Encargada de moldes.'

		},
		{
			'author': {'username': 'Ivan'},
			'body': 'El peñita.'

		}
	]
	return render_template('index.html',title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if currents_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
	login_user()
	return redirect(url_for('index'))

