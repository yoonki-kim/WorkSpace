class Person:
    count = 0
    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print('{0} created.'.format(cls.count))

    #@staticmethod
    def print_count1():
        print('{0} created.'.format(Person.count))

james = Person()
maria = Person()
richard = Person()

Person.print_count()
Person.print_count1()
