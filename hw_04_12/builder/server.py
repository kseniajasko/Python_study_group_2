from copy import deepcopy

import requests
from flask import Blueprint, request, abort, render_template, Response, url_for, redirect

from .builder import *
from ..utils.bubble_sort import bubble_sort
from ..utils.insertion_sort import *


bp = Blueprint('person', __name__)
@bp.route('/', methods=["GET", "POST"])
def person_list():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        nickname = request.form["nickname"]

        try:
            new_person = Person(email=email, password=password, nickname=nickname)
            new_person.dump_json()
            message = f"User {nickname} created!"

        except ValueError:
            return Response("Wrong nickname", status=400)

        except Warning:
            return Response("Wrong email", status=400)

    return render_template('index.html', message=message)

@bp.route('/<nickname>', methods=['GET', 'POST'])
def person_detail(nickname):
    if request.method == "GET":
        for person in Person.persons:
            if person.nickname == nickname:
                if request.method == 'GET':
                    return render_template('nickname.html', person=person)

        else:
            abort(404)
    else:
        email = request.form["email"]
        avatar = request.form["avatar"]
        nickname = request.form["nickname"]
        for person in Person.persons:
            if person.email == email:
                person.avatar = avatar
                person.dump_json()
                return render_template('nickname.html', person=person)


@bp.route('/<nickname>/posts.html', methods=['GET', 'POST'])
def nickname_post(nickname):
    message = ""
    if request.method == "GET":
        for person in Person.persons:
            if person.nickname == nickname:
                file = f'{nickname}_posts.json'
                path_json = os.path.join(os.getcwd(), 'data/post_json', file)

                try:
                    with open(path_json, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                    return render_template('posts.html', data=data)
                except:
                    return render_template('posts.html')

    else:
        title = request.form["title"]
        content = request.form["content"]
        new_post = Post(title=title, content=content, user=nickname)
        new_post.user_post_dump_json()
        new_post.all_post_dump_json()
        message = f"{nickname}'s post  created and has number {new_post.post_id}!"

        file = f'{nickname}_posts.json'
        path_json = os.path.join(os.getcwd(), 'data/post_json', file)

        with open(path_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return render_template('posts.html', message=message, data=data)



@bp.route('/login.html', methods=["GET", "POST"])
def open_login_page():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        tmp_person = None
        for person in Person.persons:
            if person.email == email:
                tmp_person = person

        if not tmp_person:
            return render_template('index.html')

        if tmp_person.password != password:
            return Response("Wrong password", status=401)

        return redirect(f"/{tmp_person.nickname}")

    return render_template('login.html')


@bp.route('/news.html', methods=['GET'])
def news_post():
        file = 'posts.json'
        path_json = os.path.join(os.getcwd(), 'data', file)

        # try:
        with open(path_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return render_template('news.html', data=data)

        # except:
        #     return abort(404)

