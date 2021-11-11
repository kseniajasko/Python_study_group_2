from copy import deepcopy

from flask import Blueprint, request, abort, render_template

from .cv_builder import Person
from ..utils.bubble_sort import bubble_sort
from ..utils.insertion_sort import *


bp = Blueprint('person', __name__)
@bp.route('/', methods=['GET', 'POST'])
def person_list():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        new_person = Person(first_name=first_name, last_name=last_name, birth_date=birth_date)
    else:
        order = request.args.get(
            'order', default = '', type = str)
        persons = deepcopy(Person.persons)
        if order:
            bubble_sort(persons, order)
        else:
            insertion_sort(Person.persons)
    return render_template('person_list.html', persons=Person.persons)

@bp.route('/<int:person_id>', methods=['GET', 'POST'])
def person_detail(person_id):
    for person in Person.persons:
        if person.id == person_id:
            if request.method == 'POST':
                person.first_name = request.form['first_name']
                person.last_name = request.form['last_name']
                person.birth_date = request.form['birth_date']

            return render_template('person_edit.html', person=person)

    else:
        abort(404)





