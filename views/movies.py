from flask_restx import Resource, Namespace
from flask import jsonify, request
from models import Movie, MovieSchema
from setup_db import db

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id', '%%', type=int)
        genre_id = request.args.get('genre_id', '%%', type=int)
        year = request.args.get('year', '%%', type=int)
        rs = db.session.query(Movie).filter(Movie.director_id.like(director_id), Movie.genre_id.like(genre_id),
                                            Movie.year.like(year)).all()
        res = MovieSchema(many=True).dump(rs)
        return jsonify(res, 200)

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movies_ns.route('/<int:rid>')
class MoviesView(Resource):
    def get(self, rid):
        r = db.session.query(Movie).get(rid)
        sm_d = MovieSchema().dump(r)
        return jsonify(sm_d, 200)

    def put(self, rid):
        movie = Movie.query.get(rid)
        req_json = request.json
        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, rid: int):
        movie = Movie.query.get(rid)
        db.session.delete(movie)
        db.session.commit()
        return "", 204