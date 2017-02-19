from flask import Flask, jsonify, request, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def index():
	return app.send_static_file("home.html")

@app.route('/addmovie')
def addmovie():
	return render_template('movie.html')

@app.route('/movie', methods = ['POST'])
def movie():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()

	try:
		name = request.form['name']
		rating = request.form['rating']
		genre = request.form['genre']
		cursor.execute('INSERT INTO films (name,rating,genre) VALUES (?,?,?)', (name,rating,genre))
		print("hi")
		connection.commit()
		message = 'Record successfully added'
	except:
		connection.rollback()
		message = 'error in insert operation'
	finally:
		return render_template('result.html', message = message)
		connection.close()

@app.route('/movies')
def movies():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM films')
	return jsonify(cursor.fetchall())
	connection.close()
	

@app.route('/search', methods = ['GET'])
def search():
	bob = (request.args.get('name'),)
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM films WHERE name = ?', bob)
	return jsonify(cursor.fetchone())
	connection.close()



