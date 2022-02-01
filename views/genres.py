from flask_restx import Resource, Namespace
from flask import jsonify
from models import Genre, GenreSchema
from setup_db import db

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        rs = db.session.query(Genre).all()
        res = GenreSchema(many=True).dump(rs)
        return jsonify(res, 200)


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = db.session.query(Genre).get(rid)
        sm_d = GenreSchema().dump(r)
        return jsonify(sm_d, 200)
