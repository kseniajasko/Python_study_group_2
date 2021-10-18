import re

all_student = []

class Student:

    def __init__(self, first_name, last_name, email, age: int, address, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.validate(email)
        self.age = age
        self.address = address
        self.gender = gender

        all_student.append(self)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if type(age) != int:
            raise ValueError('Error age type')
        else:
            self._age = age

    def validate(self, email):
        if (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email)):
            return email
        else:
            print(f"Student {self.first_name} {self.last_name} has not a valid email address")

    def __str__(self):
        return f'[{self.first_name}, {self.last_name}, {self.email}, {self.age}, {self.address}, {self.gender}]'

    def print_student(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge:{self.age}\nAddress: {self.address}\nGender: {self.gender}\n"

    def student_age_compare(self, temp_student):
        if not isinstance(temp_student, Student):
            return f'Error Student type'
        ages_diff = self.age - temp_student.age

        if ages_diff > 0:
            return f'Student {self.first_name} {self.last_name} is older, than student {temp_student.first_name} {temp_student.last_name} for {ages_diff} years'

        elif ages_diff == 0:
            return f'Student {self.first_name} {self.last_name} is peer of student {temp_student.first_name} {temp_student.last_name}'

        else:
            return f'Student {self.first_name} {self.last_name} is younger, than student {temp_student.first_name} {temp_student.last_name} for {abs(ages_diff)} years'

    def from_dict(temp_dict: dict):
        return Student(temp_dict['first_name'], temp_dict['last_name'], temp_dict['email'], temp_dict['age'], temp_dict['address'], temp_dict['gender'])

class Group:
    total_age = 0
    current = 0

    def __init__(self, group_name, group_students = []):
        self.group_name = group_name
        self.group_students = group_students

    def __str__(self):
        return (f"{self.group_students}")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > len(self.group_students) - 1:
            raise StopIteration
        else:
            self.current += 1
            return self.group_students[self.current - 1]

    def add_student(self, student: Student):
        if isinstance(student, Student):
            self.group_students.append(student)
            self.total_age += student.age
        else:
            return ValueError('Error students')

    def print_strudents_list(self):
        counter = 1
        print(f'{self.group_name.upper()}\n')
        for student in self.group_students:
            a = student.print_student()
            print(f'Student number: {counter}\n{a}' )
            counter += 1

    def group_calculate_avg_age(self):
        return self.total_age/len(self.group_students)

class Lesson:

    def __init__(self, student: Student, data, visit, assessment = 0):
        self.student = student
        self.data = data
        self.visit = visit
        self.assessment = assessment

    def __str__(self):
        if self.assessment == 0:
            return f'Student: {self.student.first_name} {self.student.last_name}, Data: {self.data}, Visit: {self.visit}'
        else:
            return f'Student: {self.student.first_name} {self.student.last_name}, Data: {self.data}, Visit: {self.visit}, Assessment: {self.assessment}'



dict_1 = {
    'first_name': 'Sirko',
    'last_name': 'Sat',
    'email': 'sirko@gmail.com',
    'age': 3,
    'address': 'Kyiw',
    'gender': 'Cat',
          }

if __name__ == '__main__':
    student_1 = Student('Ok', 'Sat', 'kl@gmail.com', 26, 'Kyiw', 'W')
    student_2 = Student('Dm', 'Sat', 'dimi@gmail.com', 28, 'Kyiw', 'M')
    student_3 = Student.from_dict(dict_1)
    lesson_1 = Lesson(student_1, '17.10', 'yes', 5)
    group_1 = Group('First group')
    group_1.add_student(student_1)
    group_1.add_student(student_2)
    group_1.add_student(student_3)

    for some_student in group_1:
        print(some_student)

