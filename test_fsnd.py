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
    
    """
    PATCH
    """
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