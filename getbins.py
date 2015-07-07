z = []
nyq = 16384
for x in range(nyq):
	y = 44100.0 * x / nyq
	z.append(y)
	
for index, thing in enumerate(z):
	if thing < 700:
		print index, thing