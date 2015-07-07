from rtcmix import *
import utils, words
import random, sys

rtsetparams(44100, 2)
load("SPECTACLE2")

start = 0

#chosen = random.choice(words.words)
#file = chosen[1]

for thing in words.words:
	rtinput(thing[1])

	amp = 10
	env = maketable("curve", 1000, 0,0,-2, 10,1,2, 1000,0)

	dur = DUR()
	fftsize = 16384
	windowsize = fftsize * 2
	winTab = 0
	overlap = 2


	eqTab = maketable("curve", "nonorm", fftsize, 0,-90,0, 151,-90,2, 152,0,0, 153,0,2,
					  154,-90,0, 160,-90,2, 161,0,1, 162,0,2, 163,-90,0, 179,-90,2, 180,0,1,
					  181,0,2, 182,-90,0, 243,-90,2, 244,0,2, 245,-90,0, fftsize,-90)
	delayTab = maketable("random", fftsize, 0, 0, 10)
	fbTab = .99
	pan = random.random()
	
	ringdown = 50
	
	SPECTACLE2(0, 0, dur, amp * env, 1, dur * ringdown, fftsize, windowsize, winTab, overlap, 
			   eqTab, delayTab, fbTab, 0, 22050, 0, 22050, 0, 1, 0, pan)
	start += ring
	print thing