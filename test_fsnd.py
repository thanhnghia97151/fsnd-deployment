import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor

database_path = os.environ['DATABASE_URL']
database_name = os.environ['DATABASE_NAME']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

class FSNDTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = database_name
        self.database_path = database_path
        setup_db(self.app, self.database_path)
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    """
    API GET
    """ 
    def test_get_moives(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['moives'])
        
    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])   

    
    """
    POST
    """
    def test_add_new_actor(self):
        res_json = {
            'name': 'New Actor 1',
            'gender': 'Male',
            'age': 20
        }
        
        res = self.client().post('/actor', json=res_json)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_add_new_actor_404(self):
        res_json = {
            'name': '',
            'gender': '',
            'age': 0
        }
        
        res = self.client().post('/actor', json=res_json)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unable to process request')
    
    def test_add_new_movie(self):
        res_json = {
            'title': 'New Title',
            'release_date': '01/01/2024'
        }
        
        res = self.client().post('/movie', json=res_json)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_add_new_movie_404(self):
        res_json = {
            'title': '',
            'release_date': ''
        }
        
        res = self.client().post('/movie', json=res_json)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unable to process request')
    """
    PATCH
    """
    
    def test_update_new_actor(self):
        res_json = {
            'id': 1,
            'name': 'New Actor 1',
            'gender': 'Male',
            'age': 20
        }
        
        res = self.client().patch('/actor/{}'.format(res_json.get('id')), json=res_json)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_update_new_movie(self):
        res_json = {
            'id': 1,
            'title': 'New Title',
            'release_date': '01/01/2024'
        }
        
        res = self.client().patch('/movie/{}'.format(res_json.get('id')), json=res_json)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_update_movie_by_id_404(self):
        id_moive = {'id': 1231231313213123}
        res = self.client().update('/movie/{}'.format(id_moive))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False) 
        self.assertEqual(data['message'], 'Not Found')
        
    def test_update_actor_by_id_404(self):
        id_actor = {'id': 123131232132131}
        res = self.client().update('/actor/{}'.format(id_actor))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')
    
    """
    DELETE
    """    
    def test_delete_actor_by_id(self):
        id_actor = {'id': 1}
        res = self.client().delete('/actor/{}'.format(id_actor))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_delete_movie_by_id(self):
        id_moive = {'id': 1}
        res = self.client().delete('/movie/{}'.format(id_moive))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)  
        
    def test_delete_movie_by_id_404(self):
        id_moive = {'id': 1231231313213123}
        res = self.client().delete('/movie/{}'.format(id_moive))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False) 
        self.assertEqual(data['message'], 'Not Found')
    
    def test_delete_actor_by_id_404(self):
        id_actor = {'id': 123131232132131}
        res = self.client().delete('/actor/{}'.format(id_actor))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')
        
if __name__ == "__main__":
    unittest.main()