#! /usr/local/bin/python

from rtcmix import *
import utils, words
import random, sys

rtsetparams(44100, 2)
load("SPECTACLE2")

chosen = random.choice(words.words)
file = chosen[1]
rtinput(file)

amp = 20
env = maketable("curve", 1000, 0,0,-2, 10,1,2, 1000,0)

dur = DUR()
fftsize = 128
windowsize = fftsize * 2
winTab = 0
overlap = 2


eqTab = maketable("random", "nonorm", fftsize/2, "gaussian", -90, 0)
delayTab = maketable("random", fftsize/2, 0, 10, 20)
fbTab = .99
pan = random.random()

ringdown = 50
	
SPECTACLE2(0, 0, dur, amp * env, 1, dur + ringdown, fftsize, windowsize, winTab, overlap, 
		   eqTab, delayTab, fbTab, 0, 22050, 0, 22050, 0, 1, 0, pan)