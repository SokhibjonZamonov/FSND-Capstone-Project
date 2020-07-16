import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Movie, Actor

JWT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJBaV9PX0ViTHBmLUNEZUtWUUZkSiJ9.eyJpc3MiOiJodHRwczovL25kZnMyMDIwLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjA4NDE2OGFlZGIzNzAwMTM4NmIzNWYiLCJhdWQiOiJtb3ZpZV9kaXJlY3RvcnMiLCJpYXQiOjE1OTQ5MTgwMTIsImV4cCI6MTU5NDkyNTIxMiwiYXpwIjoidkg3NndZeUJqU085eDJ6bFNGMGhuWFVFZ2hLb1FRc3kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.DdImh0asi4VC2Ky4CMgS3dB0jgSr9dsY4_b8kIhK2_-p2UNO81onOXILd1k4TtsXMIaOPqisyjchoGXMv-6tn8t82-gAdda-GOLSdXi-l2G8olAH2ZzRJLDvvn7JcdtlZHN6NDORq-4wr46iFt1vXcvqGxCMuZZqswv5Bx1jedikAtjoGxCfl1ySVKbwD2xZqSaZzfkaQEFkm9YM1O-psvMLpmZoHtrSfd6kTls_zIVpD2zuGYmGwAu5MrqZJQag-usOW_1yMiYBEmQ-TGjSJiCfdzr7ynmv8xNL8LxXYlk5N8cVqCg525CNS0Pp3CYoKcP79IJlgdLL0iwEdvuWXg'

class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres2001', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

                
        self.new_actor = {
            "first_name": "Jennifer",
            "last_name": "Aniston",
            "age": 51,
            "gender": "Female"
        }

        self.new_movie = {
            "title": "Casablanca",
            "release_date": "11/26/1942",
            "director": "Michael Curtiz"
        }

        
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': JWT_TOKEN
        }

		    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # test for success behavior (actors)
    def test_actors(self):
    	req=self.client().get('/actors', self.headers)
    	data=json.loads(req.data)

    	self.assertEqual(req.status_code, 200)
    	self.assertEqual(data['success'], True)
    	self.assertTrue(data['actors'])
    
    		
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
