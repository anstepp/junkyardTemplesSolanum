import glob, os

class acidDict:

	chon = ["C", "H", "O", "N", "S"]

	acidNames = []
	AAD = {}

	def testMe(input):
		try:
			float(input)
			try:
				int(input)
			except ValueError:
				return float(input)
		except ValueError:
				pass

	for file in glob.glob("*.pdb"):
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