f = open("solanumOld.txt")
n = open("solanum.txt", "w")

for line in f:
	n.write(line.rstrip())