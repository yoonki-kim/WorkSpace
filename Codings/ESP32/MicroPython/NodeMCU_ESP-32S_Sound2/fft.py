from cmath import exp, pi
import time

def fft(x):
    cnt = len(x)
    if cnt <= 1 :
        return x
    even = fft(x[0::2])
    odd  = fft(x[1::2])
    period = [exp(-2j*pi*k/cnt)*odd[k] for k in range(cnt//2)]
    return [even[k]+period[k] for k in range(cnt//2)] + \
           [even[k]-period[k] for k in range(cnt//2)]

var = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
start = time.ticks_us()
print(" ".join("%5.3f" % abs(f) for f in fft(var)))
end = time.ticks_us()
diff = end - start
print("start: %s, end: %s, diff: %s" % (start, end, diff))
