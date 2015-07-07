#! /usr/local/bin/python

from rtcmix import *
import random, sys

import words

rtsetparams(44100, 2)
load("GRANULATE")

transTab = [
			[0.02, 0.04, 0.06, 0.08],
			[0.01, 0.03, 0.05, 0.09],
			[0.00, 0.02, 0.04, 0.06],
			[0.03, 0.05, 0.07, 0.09]
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
env = maketable("curve", 1000, 0,0,2, 250,1,0, 750,1,2, 1000,0)
current = random.choice(words.words)
file = current[1]
#print file
rtinput(file)
inTab = maketable("soundfile", "nonorm", 0, file)
inChan = 0
winStart = 0.0
winEnd = DUR() - 0.0
travRate = random.uniform(0.0001, 0.001)
grainTab = maketable("window", 1000, "hanning")
hopTime = random.uniform(0.001, 0.009)
inJit = outJit = 0
grainMin = hopTime * random.uniform(11, 33)
grainMax = grainMin * random.uniform(0.1, 0.5)
grainAmpMin, grainAmpMax = grainAmp()
grainTrans = random.uniform(0.02, 0.04)
transColl = random.choice(transTab)

GRANULATE(0, inskip, dur, amp * env, inTab, 1, inChan, winStart, winEnd, 1, travRate,
		  grainTab, hopTime, inJit, outJit, grainMin, grainMax, grainAmpMax, grainAmpMin,
		  grainTrans, transColl, 0.005, 1, 0, 1, 1)