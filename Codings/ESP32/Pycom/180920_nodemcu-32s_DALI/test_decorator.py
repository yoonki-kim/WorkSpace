def deco_func(orig_func):
    def wrap_func():
        print("before run")
        return orig_func()
    return wrap_func

def tracker(func):
    print("running")
    func()

@deco_func(tracker)
def display():
    print("after run")

#decorated_disp = deco_func(display)

display()
