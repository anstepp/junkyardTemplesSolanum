from rtcmix import *
import random
from DNAFuncs import *
import words
import sys

rtsetparams(44100, 2)
load("GRANULATE")

transTab = [
			[0.00, 0.03, 0.07, 0.10],
			[0.00, 0.04, 0.07, 0.10],
			[0.00, 0.02, 0.07, 0.10],
			[0.00, 0.05, 0.10, 1.02]
			]

dur = 2

file = "{}".format(sys.argv[1])
rtinput(file)

def grainAmp():
	x = random.uniform(0.125, 0.5)
	y = random.uniform(0.25, 0.75)
	if x > y:
		return y, x
	else:
		return x, y

inskip = 0
amp = 1
env = maketable("curve", 1000, 0,0,2, 150,1,0, 850,1,2, 1000,0)
inTab = maketable("soundfile", "nonorm", 0, file)
inChan = 0
winStart = 0.01
winEnd = DUR() - 0.01
travRate = random.uniform(0.001, 0.1)
grainTab = maketable("window", 1000, "hanning")
hopTime = 0.005
inJit = outJit = 0.0025
grainMin = hopTime * 22
grainMax = grainMin = .1
grainAmpMin = grainAmpMax = 1
grainTrans = 0 #random.uniform(-0.02, 0.02)
print file, hopTime, grainMin, grainMax, grainTrans
transColl = random.choice(transTab)

GRANULATE(0, inskip, dur, amp * env, inTab, 1, inChan, winStart, winEnd, 1, travRate,
		  grainTab, hopTime, inJit, outJit, grainMin, grainMax, grainAmpMax, grainAmpMin,
		  grainTrans, transColl, 0.005, 1, 0, 1, 1)