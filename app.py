import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth.auth_file import AuthError, requires_auth


app = Flask(__name__)

def create_app(test_config=None):
  # create and configure the app
  CORS(app)

  setup_db(app)

  # Use the after_request decorator to set Access-Control-Allow
  @app.after_request
  def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization,true")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE")
    return response


  @app.route('/', methods = ['GET'])
  def main_page():
  	return render_template('main.html')
  # Actors' section
  
  # List of all actors

  @app.route('/actors', methods = ['GET'])
  @requires_auth(permission='get:actors')
  def get_all_actors(payload):
  	actors = Actor.query.all()

  	if(len(actors) == 0):
  		abort(404)

  	list_actors = [act.format() for act in actors]
  	
  	# Jsonified data return
  	return jsonify({
  		"success": True,
  		"actors": list_actors
  		})

  @app.route('/actors', methods = ['POST'])
  @requires_auth(permission='post:actors')
  def add_new_actors(payload):
  	body = request.get_json()

  	if not ('first_name' in body, 'last_name' in body, 'age' in body, 'gender' in body):
  		abort(422)

  	first_name = body.get('first_name', None)
  	last_name = body.get('last_name', None)
  	age = body.get('age', None)
  	gender = body.get('gender', None)

  	try:
  		new_actor = Actor(first_name = first_name, last_name = last_name, age = age, gender = gender)
  		new_actor.insert()

  		return jsonify({
  			"success": True
  			})
  	except:
  		abort(422)



  # Return actors by id
  @app.route('/actors/<int:id>', methods = ['GET'])
  @requires_auth(permission='get:actors')
  def get_actor_by_id(payload, id):
  	actor = Actor.query.filter(Actor.id == id).one_or_none()

  	if(actor is None):
  		abort(404)

  	# Jsonified data return
  	
  	return jsonify({
  		"success": True,
  		"actor": actor.format()
  		})


  # Delete actor by id
  @app.route('/actors/<int:id>', methods = ['DELETE'])
  @requires_auth(permission='delete:actors')
  def delete_actor(payload, id):
  	try:
  		deleting_actor = Actor.query.filter(Actor.id == id).one_or_none()

  		deleting_actor.delete()

  		return jsonify({
  			"success": True,
  			"deleted_actor_id": id
  			})
  	except:
  		abort(422)


  # Updating actor info by id
  @app.route('/actors/<int:id>', methods = ['PATCH'])
  @requires_auth(permission='patch:actors')
  def update_actor(payload, id):
  	existing_actor = Actor.query.filter(Actor.id == id).one_or_none()

  	if existing_actor is None:
  		abort(404)

  	body = request.get_json()

  	first_name = body.get('first_name')
  	last_name = body.get('last_name')
  	age = body.get('age')
  	gender = body.get('gender')

  	if first_name is not None:
  		existing_actor.first_name = first_name
  	if last_name is not None:
  		existing_actor.last_name = last_name
  	if age is not None:
  		existing_actor.age = age
  	if gender is not None:
  		existing_actor.gender = gender
  	
  	existing_actor.update()

  	return jsonify({
  		"success": True,
  		"actor": existing_actor.format()
  		})


  #Movies section

  # Get all movies
  @app.route('/movies', methods = ['GET'])
  @requires_auth(permission='get:movies')
  def get_movies(payload):
  	movies = Movie.query.order_by(Movie.id).all()

  	if(len(movies) == 0):
  		abort(404)

  	list_of_all_movies = [movie.format() for movie in movies]

  	# Jsonified data return
  	return jsonify({
  		"success": True,
  		"movies": list_of_all_movies
  		})

  # Posting a movie
  @app.route('/movies', methods = ['POST'])
  @requires_auth(permission='post:movies')
  def add_movie(payload):
  	body = request.get_json()

  	if not ('title' in body, 'release_date' in body, 'director' in body):
  		abort(422)

  	title = body.get('title', None)
  	release_date = body.get('release_date', None)
  	director = body.get('director', None)

  	try:
  		new_movie = Movie(title = title, release_date = release_date, director = director)
  		new_movie.insert()

  		return jsonify({
  			"success": True
  			})
  	except:
  		abort(422)


  # Get a movie by id
  @app.route('/movies/<int:id>', methods = ['GET'])
  @requires_auth(permission='get:movies')
  def get_movie_by_id(payload,id):
  	movie = Movie.query.filter(Movie.id == id).one_or_none()

  	if movie is None:
  		abort(404)

  	return jsonify({
  		"success": True,
  		"movie": movie.format()
  		})

  # Delete a movie by id
  @app.route('/movies/<int:id>', methods = ['DELETE'])
  @requires_auth(permission='delete:movies')
  def delete_movie(payload, id):
  	try:
  		deleting_movie = Movie.query.filter(Movie.id == id).one_or_none()

  		deleting_movie.delete()

  		return jsonify({
  			"success": True,
  			"deleted_movie_id": id
  			})
  	except:
  		abort(422)

  # Update a movie by id
  @app.route('/movies/<int:id>', methods = ['PATCH'])
  @requires_auth(permission='patch:movies')
  def update_movie(payload, id):
  	existing_movie = Movie.query.filter(Movie.id == id).one_or_none()

  	if existing_movie is None:
  		abort(404)

  	body = request.get_json()

  	title = body.get('title')
  	release_date = body.get('release_date')
  	director = body.get('director')

  	if title is not None:
  		existing_movie.title = title
  	if release_date is not None:
  		existing_movie.release_date = release_date
  	if director is not None:
  		existing_movie.director = director

  	existing_movie.update()

  	return jsonify({
  		"success": True,
  		"movie": existing_movie.format()
  		})

  # Error Handling
  @app.errorhandler(422)
  def unprocessable(error):
  	return jsonify({
                    "success": False,
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

  @app.errorhandler(404)
  def not_found(error):
  	return jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404


  @app.errorhandler(AuthError)
  def auth_error(error):
  	return jsonify({
  		"success": False,
  		"error": error.status_code,
  		"message": error.error['description']
  		}), error.status_code

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)