import json

import requests
from flask import Blueprint, request, abort, render_template, make_response, jsonify

from .cv_builder import *

bp = Blueprint('person', __name__)

data = [Person('Satur', 'Oksana', 26), Person('Satur', 'Sirko', 4)]

@bp.route('/add-person', methods=['POST', 'GET'])
def add_person():
    req = request.get_json()

    if not req['first_name'] or not req['last_name'] or not req['birth_date']:
        res = make_response(jsonify({"error": "Error first_name or last_name or birth_date"}), 400)
        return res

    new_person = Person(req['first_name'], req['last_name'], req['birth_date'])
    res = make_response(jsonify({"message": "Pearson created", "id": new_person.id}), 201)
    return res

@bp.route('/edit-person', methods=['PATCH', 'GET'])
def edit_person():
    req = request.get_json()

    for person in Person.persons:
        if person.id == int(req['id']):
            person.first_name = req['first_name']
            person.last_name = req['last_name']
            person.birth_date = req['birth_date']
            res = make_response(jsonify({"message": "Person updated"}), 201)
            return res
    else:
        res = make_response(jsonify({"error": "Pearson not found"}), 400)
        return res

@bp.route('/', methods=['GET', 'POST'])
def person_list():
    if request.method == 'GET':
        tmp_list = []
        if len(Person.persons) != 0:
            for person in Person.persons:
                tmp_list.append(str(person))
        else:
            for person in data:
                tmp_list.append(str(person))

        return json.dumps(tmp_list)

@bp.route('/<int:person_id>')
def person_detail(person_id):
    for person in Person.persons:
        if person.id == person_id:
            return person.to_json()
    else:
        abort(404)