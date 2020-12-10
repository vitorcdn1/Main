import os

def DirFile(Path, Content):
	
	dire, exte = list(), list()

	for c in content:
	
		if os.path.isdir(Path + "/" + c) == True:
			
			if c not in dire:
				dire.append(c)

		if os.path.isfile(Path + "/" + c) == True:
			
			if os.path.splitext[c][-1].replace(".", "") not in exte:
				if os.path.splitext(c)[-1] != "":
					exte.append(os.path.splitext(c)[-1]).replace(".","")
				else:
					exte.append("outros")
			if len(dire) >= 1:
				if "pasta" not in exte:
					exte.append("pasta")

	return dire, exte



