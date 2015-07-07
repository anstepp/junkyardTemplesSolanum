from rtcmix import *

rtsetparams(44100, 2)
load("STEREO")

rtinput("../snd/SolanumFull.wav")

STEREO(0, 0, DUR(), 0.66, 0.5, 0.5)