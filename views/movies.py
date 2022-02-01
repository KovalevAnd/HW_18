from flask_restx import Resource, Namespace
from flask import jsonify
from models import Movie, MovieSchema
from setup_db import db

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        rs = db.session.query(Movie).all()
        res = MovieSchema(many=True).dump(rs)
        return jsonify(res, 200)


@movies_ns.route('/<int:rid>')
class MoviesView(Resource):
    def get(self, rid):
        r = db.session.query(Movie).get(rid)
        sm_d = MovieSchema().dump(r)
        return jsonify(sm_d, 200)
