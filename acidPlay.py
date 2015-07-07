#! /usr/local/bin/python

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

dur = int(sys.argv[1])

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
current = random.choice(words.words)
file = current[1]
rtinput(file)
inTab = maketable("soundfile", "nonorm", 0, file)
inChan = 0
winStart = 0.0
winEnd = DUR() - 0.0
travRate = random.uniform(0.001, 0.1)
grainTab = maketable("window", 1000, "hanning")
hopTime = random.uniform(0.001, 0.009)
inJit = outJit = 0.0025
grainMin = hopTime * random.uniform(11, 33)
grainMax = grainMin * random.uniform(0.1, 0.5)
grainAmpMin, grainAmpMax = grainAmp()
grainTrans = random.uniform(-0.02, 0.02)
#print file, grainTrans, hopTime, grainMin, grainMax, grainTrans
transColl = random.choice(transTab)

GRANULATE(0, inskip, dur, amp * env, inTab, 1, inChan, winStart, winEnd, 1, travRate,
		  grainTab, hopTime, inJit, outJit, grainMin, grainMax, grainAmpMax, grainAmpMin,
		  grainTrans, transColl, 0.005, 1, 0, 1, 1)