import random, glob, os

r = random
r2 = random

geneTab = {
			"A" : 1,
			"C" : 2,
			"G" : 3,
			"T" : 4
			}

atomTab = {
			"C" : 14,
			"H" : 1,
			"O" : 8,
			"N" : 7,
			"S" : 16
		  }

codonTab = {"phenylalanine" : ["TTT", "TTC"],
			"leucine" : ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
			"isoleucine" : ["ATT", "ATC", "ATA"],
			"methionine" : ["ATG", ],
			"valine" : ["GTT", "GTC", "GTA", "GTG"],
			"serine" : ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
			"proline" : ["CCT", "CCC", "CCA", "CCG"],
			"threonine" : ["ACT", "ACC", "ACA", "ACG"],
			"alanine" : ["GCT", "GCC", "GCA", "GCG"],
			"tyrosine" : ["TAT", "TAC"],
			"Ochre" : ["TAA", ],
			"Amber" : ["TAG", ],
			"histidine" : ["CAT", "CAC"],
			"glutamine" : ["CAA", "CAG"],
			"asparagine" : ["AAT", "AAC"],
			"lysine" : ["AAA", "AAG"],
			"aspartate" : ["GAT", "GAC"],
			"glutamate" : ["GAA", "GAG"],
			"cysteine" : ["TGT", "TGC"],
			"Umber" : ["TGA", ],
			"tryptophan" : ["TGG", ],
			"arginine" : ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
			"glycine" : ["GGT", "GGC", "GGA", "GGG"]
			}

acidForIndex = ["acidic", "basic", "polar", "nonpolar", "stop"]

acidTypes = {
   			 "nonpolar" : ["phenylalanine", "leucine", "isoleucine", "methionine", "valine", "proline", 
			  			 "alanine", "tryptophan", "glycine"],
			 "polar" : ["serine","threonine","tyrosine","glutamine","asparagine","cysteine"],
			 "basic" : ["histidine","lysine","arginine"],
			 "acidic" : ["aspartate", "glutamate"],
			 "stop" : ["Ochre", "Amber", "Umber"]
			 }
		
chon = ["C", "H", "O", "N", "S"]
stops = ["Ochre", "Umber", "Amber"]
nucleotides = ["adenine", "cytosine", "guanine", "thymine"]

acidNames = []
AAD = {}

def testMe(input):
	try:
		float(input)
		try:
			int(input)
		except ValueError:
			return str(input.rstrip())
	except ValueError:
			pass

for file in glob.glob("*.pdb"):
	testFile = file[:len(file)-4]
	if testFile in nucleotides:
		pass
	else:
		f = open(file)
		aaName, throwMeAway = os.path.splitext(file)
		acidNames.append(aaName)
		finTab = []
		for x in f:
			var = x.rsplit(" ")
			currentTab = []
			for thing in var:
				if thing in chon:
					currentTab.append(thing)			
				else:
					testedVar = testMe(thing)
					if testedVar is not None:
						currentTab.append(testedVar)
			if currentTab:
				finTab.append(currentTab)
		AAD[aaName] = finTab
	
def getAminoAcid(codonIn):
	#print codonIn
	for key, value in codonTab.iteritems():
		#print key, value, codonIn
		if (codonIn in value):
			#print "OK,", codonIn, key
			return key
			
def getAcidData(codonIn):
	acid = getAminoAcid(codonIn)
	if acid in stops:
		return "Stop", None
	else:
		#print acid
		data = AAD[acid]
		#print data
		try:
			if data:
				return acid, data
			else:
				pass
		except (ValueError, KeyError):
			pass
		
def checkOrder(a, b):
	if a > b:
		return b, a
	else:
		return a, b		
		
def returnStuff(input):
	toTest = getAminoAcid(input) 
	for item in acidTypes:
		if toTest in acidTypes[item]:
			return (acidForIndex.index(item) + 1) * 10			