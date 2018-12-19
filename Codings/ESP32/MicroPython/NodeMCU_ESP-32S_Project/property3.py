class Test:
    def __init__(self):
        self.__color = 'red'

    @property
    def color(self):
        return self.__color

    # @color.setter
    # def color(self, var):
    #     self.__color = var

test = Test()

print('test.color : ', test.color)
# test.color = "blue"
# print('test.color : ', test.color)
test.__color = 'blue'
print('test.__color :', test.__color)
print('test.color : ', test.color)
