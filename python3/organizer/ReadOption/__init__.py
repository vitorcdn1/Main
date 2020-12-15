import colored
import os
import platform

def clear():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

class Table:

	def __init__(self, palavra, char, num):

		self.char = char
		self.num = num
		self.palavra = palavra

	def ShowTitle(self):
		print(f"{self.char * self.num} {self.palavra} {self.char * self.num}")

	def CloseTitle(self):

		result = self.num * 2 + 2 (len(self.palavra))
		print(self.char * result)

class ReadOption:

	def __init__(self, option = list()):
		self.option = option


	def ShowOption(self):
		if self.option != []:
			for c in range(0, len(self.option)):
				print(f"{c} - {self.option[c]}")

	def ReadOption(self):
		if self.option == []:
			while True:
				num = input()
				if num.isnumeric() == True:
					return int(num)
				else:
					clear()
					print(colored.colored("Error type a real number", "red"))
					break
		else:
			num_option = list()

			for c in range(0, len(self.option)):
				num_option.append(c)

			while True:
				num = input()
				if num.isnumeric() == True:
					if num in num_option:
						return int(num)
					else:
						clear()
						print(colored.colored("Error type a real option"))
						break
