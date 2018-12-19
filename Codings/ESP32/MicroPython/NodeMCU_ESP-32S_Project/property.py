class Test:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 6
        self._protected_field = 7
    def __private_method(self):
        print('__private_method')

t = Test()
t.public_field = 10
t.__private_field = 11
t._protected_field = 12

print(t.public_field,t.__private_field, t._protected_field)
t.__private_method()
