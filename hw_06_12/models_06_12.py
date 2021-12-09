import json
import os
import os.path

import string
import time
import random


def my_decorator(func):
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        try:
            start_time = time.perf_counter()
            func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Функція {func.__name__}  виконана за {run_time:.4f} секунд")
        except RuntimeError as e:
            print(str(e))
    return wrapper


work_time = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
work_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

class Doctor:
    doctors = []

    def __init__(self, doctor_name, work_day):
        self.doctor_id = len(Doctor.doctors)+1
        self.doctor_name = doctor_name
        self.work_day = work_day
        Doctor.doctors.append(self)

    def __repr__(self):
        return f'{self.doctor_name}'

    def free_doctor_time(self):
        busy_time_dict = dict()
        free_time_dict = dict()

        for day in self.work_day:
            busy_time_dict[day] = []
            free_time_dict[day] = []

        for item in Visit.visits:
            # tmp_work_time = work_time.copy()
            if item.doctor.doctor_name == self.doctor_name:
                busy_time_dict[item.day_of_week].append(item.time)

        for day in self.work_day:
            for time in work_time:
                if not time in busy_time_dict[day]:
                    free_time_dict[day].append(time)

        return free_time_dict

class Visit:
    visits = []
    # dict_visits = dict()

    def __init__(self, doctor: Doctor, day_of_week, time, client):
        self.visits_id = len(Visit.visits)+1
        self.doctor = doctor
        self.day_of_week = day_of_week
        self.time = time
        self.client = client
        Visit.visits.append(self)
        self.all_visits_dump_json()
        self.doctor_visit_dump_json()

        # if not doctor.doctor_name in Visit.dict_visits.keys():
        #     Visit.dict_visits[doctor.doctor_name] = [self]
        # else:
        #     Visit.dict_visits[doctor.doctor_name].append(self)

    @property
    def doctor_name(self):
        return self._doctor

    @doctor_name.setter
    def doctor_name(self, tmp_name):
        if isinstance(tmp_name, Doctor):
            self._doctor  = tmp_name
        else:
            raise ValueError('Doctor is not exist')

    @property
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, tmp_day):
        if not tmp_day in work_day:
            raise ValueError('Wrong day')

        if tmp_day in self.doctor.work_day:
            self._day_of_week = tmp_day
        else:
            raise ValueError(f'Doctor  work only in this day: {self.doctor.work_day}!')

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, tmp_time):
        if not tmp_time in work_time:
            raise ValueError('Wrong time')

        for item in Visit.visits:
            if tmp_time == item.time and self.doctor.doctor_name == item.doctor.doctor_name and \
                    self.day_of_week == item.day_of_week:
                raise ValueError('Time is unavailable. Select another time, day or doctor.')

        self._time = tmp_time

    def __repr__(self):
        return f'({self.doctor}, {self.day_of_week}, {self.time}, {self.client})'

    def all_visits_dump_json(self):
        file = f'all_visits.json'
        path_json = os.path.join(os.getcwd(), 'data', file)
        tmp_list = []
        for i in self.visits:
            temp_dict = {}

            temp_dict['doctor_name'] = i.doctor.doctor_name
            temp_dict['work_day'] = i.doctor.work_day
            temp_dict['day_of_week'] = i.day_of_week
            temp_dict['time'] = i.time
            temp_dict['client'] = i.client
            tmp_list.append(temp_dict)
        with open(path_json, 'w', encoding='utf-8') as file:
            json.dump(tmp_list, file, indent=4)
            file.close()

    def doctor_visit_dump_json(self):
        file = f'{self.doctor.doctor_name}.json'
        path_json = os.path.join(os.getcwd(), 'data', file)
        tmp_list = []
        for i in self.visits:
            if i.doctor.doctor_name == self.doctor.doctor_name:
                temp_dict = {}
                temp_dict['doctor_name'] = i.doctor.doctor_name
                temp_dict['work_day'] = i.doctor.work_day
                temp_dict['day_of_week'] = i.day_of_week
                temp_dict['time'] = i.time
                temp_dict['client'] = i.client
                tmp_list.append(temp_dict)
        with open(path_json, 'w', encoding='utf-8') as file:
            json.dump(tmp_list, file, indent=4)
            file.close()

    @staticmethod
    def load_doctor_from_json():
        file = 'all_visits.json'
        path_json = os.path.join(os.getcwd(), 'data', file)
        try:
            with open(path_json, 'r', encoding='utf-8') as file:
                data = json.load(file)

                for item in data:
                    tmp_doctor = Doctor(item['doctor_name'], item['work_day'])
                    Visit(tmp_doctor, item['day_of_week'], item['time'],  item['client'])
        except:
            raise ValueError('Empty file')

def randomword():
    length = 10
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@my_decorator
def add_visit(number):
    for i in range(number):
        client = randomword()
        tmp_doctor = Doctor.doctors[random.randint(0, len(Doctor.doctors) - 1)]
        tmp_time = work_time[random.randint(0, len(work_time) - 1)]
        tmp_day_of_visit = work_day[random.randint(0, len(work_day) - 1)]
        tmp_visit = Visit(tmp_doctor, tmp_day_of_visit,  tmp_time, client)






if __name__ == '__main__':
    d1 = Doctor('Doctor1', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    d2 = Doctor('Doctor2',   ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    d3 = Doctor('Doctor3', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    d4 = Doctor('Doctor4', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    d5 = Doctor('Doctor5', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    d6 = Doctor('Doctor6',   ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    d7 = Doctor('Doctor7', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    d8 = Doctor('Doctor8', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    d9 = Doctor('Doctor9', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    d10 = Doctor('Doctor10', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    # Visit.load_doctor_from_json()
    add_visit(10)
    print(Visit.visits)




