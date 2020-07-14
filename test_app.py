import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres2001', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

		    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # test for success behavior (actors)
    def test_retrived_actors(self):
    	res=self.client().get('/actors')
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['success'], True)
    	self.assertTrue(data['actors'])

    def test_retrived_actor_by_id(self):
    	res=self.client().get('/actors/1')
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['first_name'], 'Jason')
    	self.assertEqual(data['last_name'], 'Statham')
    	self.assertEqual(data['age'], 52)

    # Not found errorhandler
    def test_retrived_actor_by_id_errH(self):
    	res=self.client().get('/actors/10000')
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 404)

    def test_deleted_actor(self):
    	res=self.client().delete('/actors/2', self.headers)
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertTrue(data['success'], True)

    # Unprocessable errorhandler
    def test_deleted_actor_by_id_errH(self):
    	res=self.client().get('/actors/10000', self.headers)
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 422)

    def test_add_new_actor(self):
    	new_actor = {
    	"first_name": "Brad",
		"last_name": "Pitt",
		"age": 56,
		"gender": "Male"
    	}

    	res = self.client().post('/actors',self.headers, json = new_actor)
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['success'], True)

    def test_updated_actor(self):
    	res = self.client().patch('/actors/5', self.headers)
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['age'], 40)
    	

    # test for success behavior (movies)
    def test_retrived_movies(self):
    	res=self.client().get('/movies')
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['success'], True)
    	self.assertTrue(data['movies'])

    def test_retrived_movie_by_id(self):
    	res=self.client().get('/movies/1')
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['title'], 'Gone with the Wind')
    	self.assertEqual(data['director'], 'Victor Fleming')

    # Not found errorhandler
    def test_retrived_actor_by_id_errH(self):
    	res=self.client().get('/movies/10000')
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 404)

    def test_deleted_movie(self):
    	res=self.client().delete('/movies/1', self.headers)
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertTrue(data['success'], True)


    # Unprocessable errorhandler
    def test_deleted_actor_by_id_errH(self):
    	res=self.client().get('/movies/10000')
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 422)

    def test_add_new_movie(self):
    	new_actor = {
    	"title": "Casablanca",
		"release_date": "11/26/1942",
		"director": "Michael Curtiz"
    	}

    	res = self.client().post('/movies', self.headers, json = new_actor)
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['success'], True)

    def test_updated_movie(self):
    	res = self.client().patch('/movies/1', self.headers)
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['title'], 'Gone with the Wind.')


    # test for failure behavior (actors)
    def test_failed_actor_by_id(self):
    	res=self.client().get('/actors/1000')
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['age'], 52)

    def test_failed_deleted_actor(self):
    	res=self.client().delete('/actors/2', self.headers)
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 422)


    def test_failed_add_new_actor(self):
    	new_actor = {
    	"first_name": "Brad",
		"last_name": "Pitt",
		"age": 56,
		"gender": "Male"
    	}

    	res = self.client().post('/actors', self.headers, json = new_actor)
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 422)

    def test_failed_updated_actor(self):
    	res = self.client().patch('/actors/5', self.headers)
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 404)


    # test for failure behaviour (movies)
    def test_failed_movie_by_id(self):
    	res=self.client().get('/movies/1')
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 404)

    def test_failed_deleted_movie(self):
    	res=self.client().delete('/movies/1', self.headers)
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code, 200)


    def test_failed_add_new_movie(self):
    	new_actor = {
    	"title": "Casablanca",
		"release_date": "11/26/1942",
		"director": "Michael Curtiz"
    	}

    	res = self.client().post('/movies', self.headers, json = new_actor)
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 422)

    def test_failed_updated_movie(self):
    	res = self.client().patch('/movies/1', self.headers)
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 404)

    
    		
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
