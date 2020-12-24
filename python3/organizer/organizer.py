import os
import platform
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *

print("Programa em desenvolvimento e pode apresentar bugs ...")
print("blz fabricio")
print(f"O seu sistema é {platform.platform()}")


def ReturnSystem():
	"""
	Create a global variable with the slash of the system that you are using.
	"""
	Windows = "\\"
	Linux = "/"

	global sistema

	if platform.platform() != "Linux":
		sistema = Windows
		print(sistema)
		
	else:
		sistema = Linux
		print(sistema)

def DirFile(Path, Content):
	"""
		Return 2 variables:

		dire = that variable return all the directory inside the directory which it is inside "Path" argument.
		exte = Return all the extensions that exist inside the directory which it is inside "Content" argument.
	"""

	ReturnSystem() # Generate the variable that says wich system you are using

	dire, exte = list(), list()

	for c in content:

		if os.path.isdir(Path + sistema + c) == True:
		
			if c not in dire:
				dire.append(c)

		if os.path.isfile(Path + sistema + c) == True:
		
			if os.path.splitext(c)[-1].replace(".", "") not in exte:
				if os.path.splitext(c)[-1] != '':
					exte.append(os.path.splitext(c)[-1].replace(".",""))
				else:
					if "outros" not in exte:
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

	global undo
	undo = list()

	os.chdir(directory)
	PathPastaOrganizada = directory + sistema + "Pasta Organizada"

	try:
		
		try:
			os.mkdir("Pasta Organizada")
			os.chdir("Pasta Organizada")

		except:
			for c in Ext:
				os.rmdir(PathPastaOrganizada + sistema + c)
				
			os.rmdir(PathPastaOrganizada)
			os.mkdir("Pasta Organizada")
			os.chdir("Pasta Organizada")


			for a in content:
				
				if os.path.isdir(directory + sistema + a) == True and c == "pasta":	 # para mover as pastas
					Lugar = directory + sistema + a
					os.rename(Lugar, PathPastaOrganizada + sistema + "pasta" + sistema + a)
					undo.append([Lugar, PathPastaOrganizada + sistema + "pasta" + sistema + a])

				if os.path.splitext(a)[-1].replace(".", "") == c:				# para mover os arquivos com extenções

					begin = directory
					end = PathPastaOrganizada + sistema + c


					os.rename(begin + sistema + a, end + sistema + a)
					undo.append([begin + sistema + a, end + sistema + a])
				
				if os.path.isfile(directory + sistema + a) == True and c == "outros":
					Lugar = directory + sistema + a
					os.rename(Lugar, PathPastaOrganizada + sistema + "outros" + sistema + a)
					undo.append([Lugar, PathPastaOrganizada + sistema + "outros" + sistema + a])

	except Exception as err:
		showerror(title = "Erro", message = "Pasta já foi organizada")
		print(f"O erro foi ({err})")
	
def Undo():

	for envio, receber in undo:
		os.rename(receber, envio)

	
root = Tk()
root.title("Organizador")

ButtonDir = Button(root, text = "Abrir Pasta para organizar", font = ("Helvetica", 15), command = OpenDir)
ButtonStatus = Button(root, text = "Mostrar informações sobre a Pasta selecionada", font = ("Helvetica", 15), command = ShowStatus)
ButtonOrganize = Button(root, text = "Organizar",font = ("Helvetica", 15), command = Organize)
ButtonTest = Button(root, text = "Botão Desfazer Tudo", font = ("Helvetica", 15), command = Undo)

LabelDir = Label(root, text = "Diretorio não selecionado", font = ("Helvetica", 15))
LabelStatus = Label(root, text = "O Status irá aparece aqui", font = ("Helvetica", 20))

ButtonDir.pack(side = TOP, expand = NO, pady = 5, padx = 5)
ButtonStatus.pack(side = TOP, expand = NO, pady = 5, padx = 5)
ButtonOrganize.pack(side = TOP, expand = NO, pady = 5, padx = 5)
ButtonTest.pack(side = TOP, expand = NO, pady = 5, padx = 5)

LabelStatus.pack(side = TOP, expand = NO, pady = 5, padx = 5)
LabelDir.pack(side = BOTTOM)

root.mainloop()
