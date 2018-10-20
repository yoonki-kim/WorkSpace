class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'Hello.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.school = 'myschool'