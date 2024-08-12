from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import os

from models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    
    CORS(app)
    
    @app.after_request
    def add_access_control(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'ContentType,Authorization, True')

        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,POST,PUT,DELETE,UPDATE,OPTIONS')

        return response
    
    """
    /GET
    """
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        print(True)
        movies = Movie.query.all()
        
        movies_format = [movie.format() for movie in movies]
        
        if len(movies) == 0 or movies is None:
            abort(404)
            
        return jsonify({
            'success': True,
            'movies': movies_format
            })
        
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actor.query.all()
        
        actors_format = [actor.format() for actor in actors]
        
        if len(actors) == 0 or actors is None:
            abort(404)
            
        return jsonify({
            'success': True,
            'actors': actors_format
        })
    
    """
    /POST
    """
    @app.route('/movie', methods=['POST'])
    @requires_auth('post:movie')
    def add_movie(payload):
        res = request.get_json()
        res_title = res.get('title')
        res_release_date = res.get('release_date')
        
        movie = Movie(title=res_title,
                      release_date=res_release_date)
        
        try:
            if (res_title and res_release_date) is None:
                abort(422)
                
            movie.insert()
        except:
            abort(422)
            
        return jsonify({
                    'success': True
                })
    
    @app.route('/actor', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor(payload):
        res = request.get_json()
        res_name = res.get('name')
        res_gender = res.get('gender')
        res_age = res.get('age')
        
        actor = Actor(name=res_name,
                      gender=res_gender,
                      age=res_age)
        
        try:
            if (res_name and res_gender and res_age) is None:
                abort(422)
            actor.insert()
        except:
            abort(422)
        
        return jsonify({
            'success': True
        }) 
    """
    /PATCH
    """
    @app.route('/movie/<id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_moive(payload, id):
        res = request.get_json()
        
        query_movie = Movie.query.get(id)
        
        if query_movie is None:
            abort(404)
            
        res_title = res.get('title')
        res_release = res.get('release_date')    
        
        try:
            query_movie.title = res_title
            query_movie.res_release = res_release
            
            query_movie.update()
        except:
            abort(422)
        
        return jsonify({
            'success': True
        })

    @app.route('/actor/<id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(payload, id):
        res = request.get_json()
        
        query_actor = Actor.query.get(id)      
        
        if query_actor is None:
            abort(404)
        
        res_name = res.get('name')
        res_gender = res.get('gender')
        res_age = res.get('age')
        
        try:
            query_actor.name = res_name
            query_actor.gender = res_gender
            query_actor.age = res_age
            
            query_actor.update()
        except:
            abort(422)
        return jsonify({
            'success': True
        })
    """
    /DELETE
    """  
    @app.route('/actor/<id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload,id):
        query_actor = Actor.query.get(id)
        
        if query_actor is None:
            abort(404)
            
        try:
            query_actor.delete()
        except:
            abort(422)
            
        return jsonify({
            'success': True
        })
    @app.route('/movie/<id>', methods=['DELETE'])    
    @requires_auth('delete:movie')
    def delete_moive(payload, id):
        query_movie = Movie.query.get(id)
        
        if  query_movie is None:
            abort(404)
        
        try:
            query_movie.delete()
        except:
            abort(422)
            
        return jsonify({
            'success': True
        })
    """
    Handler ERROR
    """ 
    @app.errorhandler(404)
    def error_404(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404

    @app.errorhandler(422)
    def error_422(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unable to process request'
        }), 422
        
    @app.errorhandler(400)
    def error_400(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request',
        }), 400
        
    @app.errorhandler(500)
    def error_500(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'
        }), 500
        
    @app.errorhandler(AuthError)
    def handler_auth_error(e):
        return jsonify({
            "success": False,
            "error": e.status_code,
            "message": e.error
        })    
        
    return app

    
    
    
        
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
