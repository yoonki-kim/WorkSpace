class Test:
    def __init__(self):
        self.__color = "red"

    @property  # get
    def color(self):
        return self.__color

    @color.setter  #set
    def color(self, var):
        self.__color = var


# t = Test()
# t.color = "blue"
# print(t.color)

test = Test()
print('test.color_old : ', test.color)
test.color = "blue"
print('test.color_new : ', test.color)
