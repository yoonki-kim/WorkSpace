def trace1(func):
    def wrapper():
        print('Start trace 1')
        func()
        print('End trace 1')
    return wrapper

def trace2(func):
    def wrapper():
        print('Start trace 2')
        func()
        print('End trace 2')
    return wrapper

@trace1
@trace2
def hello():
    print('hello')

# @trace
# def world():
#     print('world')

#trace_hello = trace(hello)
#trace_hello()
#trace_world = trace(world)
#trace_world()

hello()
# world()
