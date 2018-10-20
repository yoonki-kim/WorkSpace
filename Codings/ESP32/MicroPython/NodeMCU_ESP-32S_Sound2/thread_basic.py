# Thread basic
import _thread
import time

def th_func(delay, id):
    while True:
        time.sleep(delay)
        print('Running thread %d, delay %d' % (id, delay))

for i in range(3):
    _thread.start_new_thread(th_func, (i+1, i))
