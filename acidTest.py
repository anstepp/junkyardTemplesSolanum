import words
from multiprocessing import Process
from subprocess import Popen
import time

start = 0

for item in words.words:

	passMe = "pycmix -q < acidTest2.py {} ".format(str(item[1]))
	
	Popen(passMe + str(start), shell=True)
	
	time.sleep(6)