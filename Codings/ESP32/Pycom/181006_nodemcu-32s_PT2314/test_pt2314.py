from pt2314 import PT2314
import time

audio = PT2314()

audio.setAttenuation(70,70)
time.sleep(0.1)
audio.setVolume(70)
