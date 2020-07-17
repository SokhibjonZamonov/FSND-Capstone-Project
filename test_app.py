import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Movie, Actor

JWT_TOKEN = 'token'


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'postgres2001', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_actor = {
            "first_name": "Jennifer",
            "last_name": "Aniston",
            "age": 51,
            "gender": "Female"
        }

        self.new_movie = {
            "title": "How to Train Your Dragon",
            "release_date": "1/3/2019",
            "director": "Dean DeBlois"
        }

        self.new_movie1 = {
            "title": "Once Upon a Time in Hollywood",
            "release_date": "7/24/2019",
            "director": "Quentin Tarantino"
        }

        self.edit_actor = {
            "age": 82
        }

        self.edit_movie = {
            "title": "Casablanca 1"
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # Tests for GET requests (actors)
    def test_actors(self):
        req = self.client().get('/actors', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_actors_by_id(self):
        req = self.client().get('/actors/1', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    # Test for POST request (actors)
    def test_adding_actors(self):
        req = self.client().post('/actors', json=self.new_actor, headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)

    # Test for PATCH request (actors)
    def test_updating_actors(self):
        req = self.client().patch('/actors/1', json=self.edit_actor, headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        }, )
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    # Test for DELETE request (actors)
    def test_delete_actor(self):
        req = self.client().delete('/actors/8', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_actor_id'], 8)

    # Test for POST requests (movies)
    def test_add_movies(self):
        req = self.client().post('/movies', json=self.new_movie, headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)

    # Tests for GET requests (movies)
    def test_get_movies(self):
        req = self.client().get('/movies', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_movies_by_id(self):
        req = self.client().get('/movies/10', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Test for PATCH request (movies)

    def test_update_movie(self):
        req = self.client().patch('/movies/5', json=self.edit_movie, headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    # Test for DELETE request (movies)
    def test_delete_movies(self):
        req = self.client().delete('/movies/6', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_movie_id'], 6)

    # Tests for failures (actors)
    def test_not_found_actors(self):
        req = self.client().delete('/actors/1000', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 404)

    def test_failed_del_actors(self):
        req = self.client().delete('/actors/1000', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 422)


    def test_failed_add_actors(self):
        req = self.client().post('/actors', json={"first_name": unknown}, headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 422)


    # Tests for failures (movies)
    def test_not_found_movies(self):
        req = self.client().delete('/movies/1000', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 404)

    def test_failed_del_movies(self):
        req = self.client().delete('/movies/1000', headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 422)

    def test_failed_add_movies(self):
        req = self.client().post('/movies', json={"title": unknown}, headers={
            "Authorization": "Bearer {}".format(JWT_TOKEN)
        })
        data = json.loads(req.data)

        self.assertEqual(req.status_code, 422)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
