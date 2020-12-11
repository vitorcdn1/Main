from os import system

try:
	NameFile = input("Type the Name of the file: ")
	
	system(f"g++ {NameFile} -o {NameFile[:-4]}")
	print("="*50)
	system(f"./{NameFile[:-4]}")

except Exception as err:
	print("Erro")
