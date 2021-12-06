import json
import operator
import os
import re

json_all_users = 'users.json'
json_all_posts = 'posts.json'

class Person:

    persons = []

    def __init__(self, email, password, nickname, avatar=None):
        self.id = str(len(Person.persons) + 1)
        self.email = email
        self.password = password
        self.nickname = nickname
        self.avatar = avatar
        Person.persons.append(self)


    @property
    def email(self):
        return self._email


    @email.setter
    def email(self, current_email):
        for item in Person.persons:
            if item.email == current_email:
                raise Warning("Email exist")

        if (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$",
                     current_email)):
            self._email = current_email
        else:
            raise Warning("Wrong email")

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, current_nickname):
        if str.isalnum(current_nickname):
            self._nickname = current_nickname
        else:
            raise ValueError("Wrong nickname")

    def __repr__(self):
        return f"({self.email}, {self.password}, {self.nickname})"

    def dump_json(self):
        path_json = os.path.join(os.getcwd(), 'data', json_all_users)
        person_list = [t.__dict__ for t in self.persons]
        with open(path_json, 'w', encoding='utf-8') as file:
            json.dump(person_list, file, indent=4)
            file.close()

    @staticmethod
    def load_data_from_json():
        path_json = os.path.join(os.getcwd(), 'data', json_all_users)
        try:
            with open(path_json, 'r', encoding='utf-8') as file:
                data = json.load(file)

                for item in data:
                    Person(item['_email'], item['password'], item['_nickname'], item['avatar'])
        except:
            print('Empty file')

class Post:

    posts = []

    def __init__(self, title, content, user):
        self.post_id = len(Post.posts) + 1
        self.title = title
        self.content = content
        self.user = user
        Post.posts.append(self)

    def __repr__(self):
        return f"({self.post_id}, {self.title}, {self.content}, {self.user})"

    def user_post_dump_json(self):
        file = f'{self.user}_posts.json'
        path_json = os.path.join(os.getcwd(), 'data\post_json', file)
        user_post_list = [t.__dict__ for t in self.posts if t.user == self.user]
        sorted_user_post_list = sorted(user_post_list, key= operator.itemgetter('post_id'), reverse=True)
        with open(path_json, 'w', encoding='utf-8') as file:
            json.dump(sorted_user_post_list, file, indent=4)
            file.close()

    def all_post_dump_json(self):
        path_json = os.path.join(os.getcwd(), 'data', json_all_posts)
        posts_list = [t.__dict__ for t in self.posts]
        sorted_post_list = sorted(posts_list, key=operator.itemgetter('post_id'), reverse=True)
        with open(path_json, 'w', encoding='utf-8') as file:
            json.dump(sorted_post_list, file, indent=4)
            file.close()

    @staticmethod
    def load_post_from_json():
        path_json = os.path.join(os.getcwd(), 'data', json_all_posts)
        try:
            with open(path_json, 'r', encoding='utf-8') as file:
                data = json.load(file)

                for item in data:
                    Post(item['title'], item['content'], item['user'])
        except:
            print('Empty file')








