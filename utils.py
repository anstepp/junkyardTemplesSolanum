from rtcmix import *
import random

#--lfo table

lfoTypes = ["sine", "saw", "sawup", "tri"]
saws = ["saw" + str(x) for x in range(2, 51)]
tris = ["tri" + str(x) for x in range(2, 51)]
lfoTypes += saws
lfoTypes += tris

def getLFO():
	wave = random.choice(lfoTypes)
	freq = random.uniform(1, 20)
	amp = random.uniform(.5, 10)
	return wave, freq, amp

#--trem or vib

def tremOrVib(prob):
	if prob > 100:
		prob = 100
	if prob < 0:
		prob = 0
	test = random.randint(0, 100)
	if test < prob:
		return "vib"
	elif test > prob:
		return "trem"
	else:
		return "both"
		
