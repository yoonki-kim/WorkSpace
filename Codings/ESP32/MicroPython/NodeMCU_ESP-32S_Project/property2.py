class Test:
    def __init__(self):
        self.color = 'red'
    def set_color(self, var):
        self.color = var
    def get_color(self):
        return self.color

test = Test()

print('test.color : ', test.color)
test.set_color("blue")
print('test.get_color : ', test.get_color())
