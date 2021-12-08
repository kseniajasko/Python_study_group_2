import json
import os
import os.path



class Doctor:
    doctors = []

    def __init__(self, doctor_name, work_day):
        self.doctor_id = len(Doctor.doctors)+1
        self.doctor_name = doctor_name
        self.work_day = work_day
        Doctor.doctors.append(self)

    def __repr__(self):
        return f'{self.doctor_name}'

class Visit:
    visits = []

    def __init__(self, doctor: Doctor, day_of_week, time, client):
        self.doctor = doctor
        self.day_of_week = day_of_week
        self.time = time
        self.client = client
        Visit.visits.append(self)
        self.all_visits_dump_json()
        self.doctor_visit_dump_json()

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
        if tmp_day in self.doctor.work_day:
            self._day_of_week = tmp_day
        else:
            raise ValueError('Doctor does not work in this day. Change day!')

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, tmp_time):
        if tmp_time in [9, 10, 11, 12, 13, 14, 15]:
            for item in Visit.visits:
                if tmp_time == item.time and self.doctor.doctor_name == item.doctor.doctor_name and \
                        self.day_of_week == item.day_of_week:
                    raise ValueError('Time is unavailable. Select another time, day or doctor.')
            self._time = tmp_time
        else:
            raise ValueError('Wrong time')

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
                    tmp_doctor = Doctor(item['doctor'], item['work_day'])
                    Visit(tmp_doctor, item['day_of_week'], item['time'],  item['client'])
        except:
            print('Empty file')



if __name__ == '__main__':
    d1 = Doctor('Satur', ['Mon', 'Tue', 'Wed'])
    d2 = Doctor('Sirko', ['Mon', 'Sat', 'Sun'])
    d3 = Doctor('Sirko', ['Mon', 'Tue', 'Sun'])
    v1 = Visit(d1, 'Mon', 9, 'OK')
    v2 = Visit(d2, 'Mon', 10, 'RM')
    v3 = Visit(d3, 'Mon', 12, 'RM1')
    v4 = Visit(d3, 'Mon', 11, 'sadshdh')
    v5 = Visit(d2, 'Sat', 15, 'RM1')
    # v3.create_visit()

    #Visit.load_doctor_from_json()




