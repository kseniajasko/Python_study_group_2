import os
import json
import csv
import googlemaps
from datetime import datetime


class OpenFile:

    def __init__(self, filename, mode):
        self._file = open(filename, mode)

    def __enter__(self):
        return self._file

    def __exit__(self, type, value, traceback):
        self._file.close()
        return True

class Maps:

    def __init__(self, key):
        self._client = googlemaps.Client(key=key)

    def __enter__(self):
        return self._client

    def __exit__(self, error_type, value, traceback):
        del self._client
        return True

class Task:

    def __init__(self, title, priority = 1):
        self.done = False
        self.title = title
        self.priority = priority
        self.location = None

    def __str__(self):
        return self.title

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if int(value) in range(1, 11):
            self._priority = value
        else:
            raise ValueError('Priority value is out of range')

    def add_location(self):
        place_lookup = input('Enter location name: \t')
        with Maps(key='AIzaSyDZUTx1HWrOcNDng1V7-smaaHTBSobrw0I') as gmaps:
            place = gmaps.find_place(
                place_lookup,
                'textquery',
                fields=['geometry/location', 'name', 'place_id']
            )
            if place['status'] == 'OK':
                self.location = {
                    'coordinates': place['candidates'][0]['geometry']['location'],
                    'name': place['candidates'][0]['name'],
                    'google_id': place['candidates'][0]['place_id']
                }


class Dashboard:

    def __init__(self):
        self.task_list = []

    def add_task(self):
        title = input('Task name:  ')
        priority = input('Priority:  ')
        new_task = Task(title, priority)
        self.task_list.append(new_task)

    def print_all_tasks(self):
        for task in self.task_list:
            print(task)

    def print_all_tasks_by_priority(self, temp_priority):
        temp_list = []
        for task in self.task_list:
            if temp_priority == task.priority:
                temp_list.append(task.title)
        return temp_list

    def sort_by_title(self):
        return sorted(self.task_list,
            key=lambda task: task.title)



    def dump_to_json(self, filename):
        task_list = [t.__dict__ for t in self.task_list]
        filepath = os.path.join(os.getcwd(),'data', filename)
        with OpenFile(filepath, 'w') as dump_file:
            json.dump(task_list, dump_file)

    def load_from_json(self, filename):
        filepath = os.path.join(os.getcwd(), 'data', filename)
        with OpenFile(filepath, 'r+') as dump_file:
            json.load(dump_file)

    def dump_csv(self, filename):
        task_list = [t.__dict__ for t in self.task_list]

        fieldnames = []
        for task in task_list[0]:
            fieldnames.append(task)

        filepath = os.path.join(os.getcwd(),'data', filename)
        with OpenFile(filepath, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(fieldnames)
            for task in task_list:
                temp_list = []
                for task_property in task.values():
                    temp_list.append(task_property)
                writer.writerow(temp_list)


    def load_csv(self, filename):
        filepath = os.path.join(os.getcwd(), 'data', filename)
        with OpenFile(filepath, 'r') as file:
            csv.reader(file, delimiter=',')


if __name__ == '__main__':
    dashboard_1 = Dashboard()
    dashboard_1.add_task()
    dashboard_1.add_task()
    dashboard_1.dump_csv('proba.csv')
    dashboard_1.load_csv('proba.csv')


