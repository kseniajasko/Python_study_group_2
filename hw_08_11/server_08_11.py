import json

from flask import Blueprint,  request, abort, render_template

from .cv_builder import *

bp = Blueprint('person', __name__)

@bp.route('/', methods=['GET', 'POST'])
def person_list():
    if request.method == 'GET':
        tmp_list = []
        if len(Person.persons) != 0:
            for person in Person.persons:
                tmp_list.append(str(person))
        else:
            data = [Person('Satur', 'Oksana', 26), Person('Satur', 'Sirko', 4)]
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