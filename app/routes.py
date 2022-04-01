from flask import render_template
from app import app

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
