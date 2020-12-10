import os
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *


def DirFile(Path, Content):
	
	dire, exte = list(), list()
	
	for c in content:

		if os.path.isdir(Path + "/" + c) == True:
		
			if c not in dire:
				dire.append(c)

		if os.path.isfile(Path + "/" + c) == True:
		
			if os.path.splitext(c)[-1].replace(".", "") not in exte:
				if os.path.splitext(c)[-1] != '':
					exte.append(os.path.splitext(c)[-1].replace(".",""))
				else:
					exte.append("outros")
			if len(dire) >= 1:
				if "pasta" not in exte:
					exte.append("pasta")

	return dire, exte

def OpenDir():
	
	global directory
	global content
	global Files
	global Ext

	directory = filedialog.askdirectory()

	
	content = os.listdir(directory)
	LabelDir["text"] = directory
		

	Files, Ext = DirFile(Path = directory, Content = content)
	
	
def ShowStatus():
	
	status = list()

	for c in Ext:
		status.append(c + "\n")

	status = "".join(status)

	LabelStatus["text"] = status
	
def Organize():

	os.chdir(directory)

	try:

		os.mkdir("Pasta Organizada")
		os.chdir("Pasta Organizada")
		PathPastaOrganizada = directory + "/" + "Pasta Organizada"

		for c in Ext:
			os.mkdir(c)
			for a in content:
				if os.splitext(a)[-1] == c:
					os.rename(directory + "/" + a, PathPastaOrganizada + c)

	except:
		showerror(title = "Erro", message = "Pasta já foi organizada")
	
	print(directory)
	

	
root = Tk()
root.title("Organizador")

ButtonDir = Button(root, text = "Abrir Pasta para organizar", font = ("Helvetica", 15), command = OpenDir)
ButtonStatus = Button(root, text = "Mostrar informações sobre a Pasta selecionada", font = ("Helvetica", 15), command = ShowStatus)
ButtonOrganize = Button(root, text = "Organizar",font = ("Helvetica", 15), command = Organize)

LabelDir = Label(root, text = "Diretorio não selecionado", font = ("Helvetica", 15))
LabelStatus = Label(root, text = "O Status irá aparece aqui", font = ("Helvetica", 20))

ButtonDir.pack(side = TOP, expand = NO, pady = 5, padx = 5)
ButtonStatus.pack(side = TOP, expand = NO, pady = 5, padx = 5)
ButtonOrganize.pack(side = TOP, expand = NO, pady = 5, padx = 5)


LabelStatus.pack(side = TOP, expand = NO, pady = 5, padx = 5)
LabelDir.pack(side = BOTTOM)

root.mainloop()
