#! /usr/local/bin/python

from Tkinter import *
import ttk

from DNAFuncs import *

import sys, time, os

from multiprocessing import Process
from subprocess import Popen

file = open("solanum.txt")

def acidPlayer():
	codon = ""
	lastPitch = 240
	for genome in file:
		for gene in genome:
			codon = codon + gene
			if len(codon) is 3:
				acid, acidData = getAcidData(codon)
				if acidData:
					for item in acidData:
						duration = atomTab[item[0]]
						pitchToPass = lastPitch + float(item[1])
						Popen("pycmix -q < acidPlay.py " + str(duration) + " " + str(pitchToPass) + " " + str(item[2]) + " " + str(item[3]), shell=True)
						lastPitch = pitchToPass
						if duration > 1:
							time.sleep(duration - random.uniform(1, 4))
						else:
							time.sleep(duration - random.random())
				codon = ""

def codonPlayer():
	codon = ""
	for genome in file:
		for gene in genome:
			codon = codon + gene
			if len(codon) is 3:
				duration = returnStuff(codon)
				passMe = "pycmix -q < codonPlay.py " + str(duration) + " " + str(duration)
				Popen(passMe, shell=True)
				codon = ""
				time.sleep(duration - random.random())

def genePlayer():
	for genome in file:
		for gene in genome:
			geneNum = geneTab[gene]
			Popen("pycmix -q < genePlay.py " + str(geneNum), shell=True)
			time.sleep(random.uniform(4, 6))
			
def textPlayer():
	while(True):
		Popen("pycmix -q < textPlay.py", shell=True)
		time.sleep(random.uniform(120, 240))

t = Process(target=acidPlayer)
u = Process(target=codonPlayer)
v = Process(target=genePlayer)
w = Process(target=textPlayer)
			
def runAudio():
	t.start()
	u.start()
	v.start()
	w.start()
	
def killAudio():
	print "Terminating Audio, will take a few seconds..."
	t.terminate()
	u.terminate()
	v.terminate()
	w.terminate()
	
def runVideo():
	Popen("processing-java --sketch=/Users/aaronstepp/Documents/Compositions/44_JunkyardTemplesSet2/WordPaintingCurrent --output=out --run --present --force", shell=True)
	
def quitProgram():
	root.quit()

if __name__ == "__main__":
	root = Tk()
	root.title("Junkyard Temples")

	content = ttk.Frame(root, padding=(3,3,12,12))
	namelbl = ttk.Label(content, text="Junkyard Temples,\n Set II: Solanum")
	
	audioFrame = ttk.Frame(content)
	audioFrame['borderwidth'] = 2
	audioFrame['relief'] = 'sunken'
	videoFrame = ttk.Frame(content)
	videoFrame['borderwidth'] = 2
	videoFrame['relief'] = 'sunken'

	audio = ttk.Button(audioFrame, text="Run Audio", command=runAudio)
	stopAudio = ttk.Button(audioFrame, text="Stop Audio", command=killAudio)
	video = ttk.Button(videoFrame, text="Run Video", command=runVideo)
	videoLabel = ttk.Label(videoFrame, text="Video quits on \'esc\'")
	quitEverything = ttk.Button(content, text="Quit", command=quitProgram)

	content.grid(column=0, row=0, sticky=(N, S, E, W))
	namelbl.grid(column=1, row=0, columnspan=2, sticky=(N, W), padx=5)
	audioFrame.grid(column=0, row=1)
	videoFrame.grid(column=3, row=1, sticky=E)
	audio.grid(column=3, row=3)
	stopAudio.grid(column=3, row=4)
	video.grid(column=4, row=3)
	videoLabel.grid(column=4, row=4)
	quitEverything.grid(column=1, row=5, sticky=(E,W))

	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)
	content.columnconfigure(0, weight=3)
	content.columnconfigure(1, weight=3)
	content.columnconfigure(2, weight=3)
	content.columnconfigure(3, weight=1)
	content.columnconfigure(4, weight=1)
	content.rowconfigure(1, weight=1)
	
	#root.withdraw()
	root.mainloop()
