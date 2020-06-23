print('__name__', __name__)
print('__pacakge__', __package__)
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .. import api
from ..database.models import setup_db, Drink

'''
To run unit tests of test_api.py
first inside ./backend/src/test run the following commands:
sqlite3 database_test.db < dummy_data.sql
then inside ./backend run the following commnands:
python3 -m src.test.test_api

Note: Unit Tests for this project already made by Postman
'''

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = api.app
        self.client = self.app.test_client
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_filename = "database_test.db"
        self.database_path = "sqlite:///{}".format(os.path.join(self.project_dir, self.database_filename))

        # binds the app to the current context
        with self.app.app_context():
            setup_db(self.app, self.database_path)
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_200_retrieving_all_drinks(self):
        res = self.client().get('/drinks')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['drinks'])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()