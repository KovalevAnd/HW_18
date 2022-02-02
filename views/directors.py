from flask_restx import Resource, Namespace
from flask import jsonify, abort
from models import Director, DirectorSchema
from setup_db import db

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = db.session.query(Director).all()
        res = DirectorSchema(many=True).dump(rs)
        return jsonify(res, 200)


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = db.session.query(Director).get(rid)
        if r is None:
            return abort(404)
        else:
            sm_d = DirectorSchema().dump(r)
            return jsonify(sm_d, 200)
