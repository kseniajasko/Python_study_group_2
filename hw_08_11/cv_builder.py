import os
import re
import json

from datetime import datetime


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return (nums)


class MultiDict:
    def __init__(self):
        self.dict = {}

    def __setitem__(self, key, value):
        try:
            self.dict[key].append(value)
        except KeyError:
            self.dict[key] = [value]

    def __getitem__(self, key):
        return self.dict[key]

    def __repr__(self):
        return f'{self.dict}'

    def keys(self):
        return self.dict.keys()


class Skill:

    def __init__(self, category, name, experience, level):
        self.category = category
        self.name = name
        self.experience = experience
        self.level = level

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, skill):
        if skill.lower() in ['technologies', 'methodologies', 'languages']:
            self._category = skill
        else:
            self._category = None

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, current_experience):
        if type(current_experience) == int:
            self._experience = current_experience
        else:
            raise ValueError('experience is not digital')

    @property
    def level(self):
        return self._category

    @level.setter
    def level(self, level):
        if level.lower() in ['beginner', 'junior', 'middle', 'senior', 'expert']:
            self._level = level
        else:
            self._level = None

    def __gt__(self, other):
        return self._experience > other._experience

    def __repr__(self):
        return f'({self.name}, {self.experience}, {self.level})'


class Contact:

    def __init__(self, contact_type, value):
        self.contact_type = contact_type
        self.value = value

    @property
    def contact_type(self):
        return self._contact_type

    @contact_type.setter
    def contact_type(self, current_contact_type):
        if current_contact_type.lower() in ['email', 'phone']:
            self._contact_type = current_contact_type
        else:
            self._contact_type = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, current_value):
        if self.contact_type.lower() == 'email':

            if (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$",
                         current_value)):
                self._value = current_value

            else:
                self._value = None
        elif self.contact_type.lower() == 'phone':
            if re.match(r'^(?:\+?44)?[07]\d{9,13}$', current_value):
                self._value = current_value
            else:
                self._value = None
        else:
            self._value = None

    def __repr__(self):
        return f'({self.contact_type}, {self.value})'


class JobExperience:

    def __init__(self, start_date, end_date, company, position):
        self.start_date = start_date
        self.end_date = end_date
        self.company = company
        self.position = position

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, current_date):
        if datetime.strptime(current_date, '%d.%m.%Y'):
            self._start_date = current_date
        else:
            raise ValueError('Wrong start date')

    @property
    def end_date(self):
        return self._start_date

    @end_date.setter
    def end_date(self, current_date):
        if datetime.strptime(current_date, '%d.%m.%Y'):
            self._end_date = current_date
        else:
            raise ValueError('Wrong end date')

    def __repr__(self):
        return f'({self.start_date}, {self.end_date}, {self.company}, {self.position})'


class Person:
    persons = []

    def __init__(self, first_name, last_name, birth_date):
        self.id = len(Person.persons) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.contacts = []
        self.skills = []
        self.experiences = []
        Person.persons.append(self)

    # def __repr__(self):
    #     all_pearson = [t.__dict__ for t in self.persons]
    #     return f'{all_pearson}'

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def all_skills(self):
        #   all_skills = [t.__dict__ for t in self.skills]
        tmp_dict = MultiDict()
        for skill in self.skills:
            tmp_dict[skill._category] = skill
        tmp_dict_sorted = dict()
        for key in tmp_dict.keys():
            tmp_dict_sorted[key] = bubble_sort(tmp_dict[key])
        return tmp_dict_sorted

    def add_contact(self, current_contact: Contact):
        if isinstance(current_contact, Contact):
            self.contacts.append(current_contact)
            return self.contacts
        else:
            raise ValueError('Wrong contact')

    def delete_contact(self, current_contact: Contact):
        for contact in self.contacts:
            if contact == current_contact:
                self.contacts.remove(current_contact)
                return True
        return False

    def add_skill(self, current_skill: Skill):
        if isinstance(current_skill, Skill):
            self.skills.append(current_skill)
        else:
            raise ValueError('Wrong skill')

    def delete_skill(self, current_skill: Skill):
        for skill in self.skills:
            if skill == current_skill:
                self.contacts.remove(current_skill)
                return True
        return False

    def add_experience(self, current_experience: JobExperience):
        if isinstance(current_experience, JobExperience):
            self.experiences.append(current_experience)
        else:
            raise ValueError('Wrong experience')

    def delete_experience(self, current_experience: JobExperience):
        for experience in self.experiences:
            if experience == current_experience:
                self.experiences.remove(current_experience)
                return True
        return False

    def sort_experience(self):
        func_date = lambda d: (datetime.strptime(d.start_date, '%d.%m.%Y')
                               - datetime.strptime(d.end_date, '%d.%m.%Y')).days
        return sorted(self.experiences, key=func_date)

    def to_json(self):
        return json.dumps(self.__dict__)

    def dump_json(self):
        file_name = 'person.json'
        path_json = os.path.join(os.getcwd(), 'data', file_name)
        person_list = str([t.__dict__ for t in self.persons])
        with open(path_json, 'w') as file:
            json.dump(person_list, file)

    @classmethod
    def load_json(cls):
        file_name = 'person.json'
        path_json = os.path.join(os.getcwd(), 'data', file_name)
        with open(path_json, 'r') as file:
            dict_person = json.load(file)
        return dict_person


if __name__ == '__main__':
    my_person = Person('Oksana', 'Satur', '03.05.1995')

    contact1 = Contact('email', 'oksana@gmail.com')
    contact2 = Contact('phone', '0956380996')
    skill_1 = Skill('technologies', 'python', 3, 'beginner')
    skill_2 = Skill('technologies', 'JS', 1, 'beginner')
    skill_4 = Skill('languages', 'ENG', 2, 'middle')
    skill_5 = Skill('languages', 'DE', 10, 'middle')
    skill_6 = Skill('methodologies', 'math', 10, 'senior')
    skill_7 = Skill('methodologies', 'math', 9, 'senior')
    exp_1 = JobExperience('01.11.2017', '31.10.2020', 'IM', 'Phd Student')
    exp_2 = JobExperience('01.11.2020', '31.10.2021', 'IM', 'Phd Researcher')
    exp_3 = JobExperience('24.08.2021', '09.11.2021', 'BT', 'Py Student')
    # husband_person = Person('Dmytro', 'Satur', '06.11.1992')
    # contact3 = Contact('email', 's.dimi.d@gmail.com')
    # skill_3 = Skill('technologies', 'JS', '6', 'middle')
    # husband_person.add_contact(contact3)
    # husband_person.add_skill(skill_3)

    my_person.add_contact(contact1)
    my_person.add_contact(contact2)
    my_person.add_skill(skill_1)
    my_person.add_skill(skill_2)
    my_person.add_skill(skill_4)
    my_person.add_skill(skill_5)
    my_person.add_skill(skill_6)
    my_person.add_skill(skill_7)
    my_person.add_experience(exp_2)
    my_person.add_experience(exp_1)
    my_person.add_experience(exp_3)
    my_person.delete_experience(exp_3)
    # print(my_person)
    # my_person.all_skills()
    # print(my_person.experiences)
    # print(my_person.sort_experience())
    my_person.dump_json()
    # print(my_person.load_json())
