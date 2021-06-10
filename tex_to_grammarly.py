
import yaml

MAX_FOR = 300

class converter():

	def __init__(self):

		self.s0 = self.read_input_text()
		self.s = self.s0

		self.letters_number = 66

		self.references_number = 1
		self.citations_number = 1

		self.config_list = ""
		self.read_config()


	def get_output():
		return self.s

	def get_input():
		return self.s0


	def read_input_text(self):

		f = open("input.txt", "r")
		s = f.read()
		f.close()

		return s

	def write_output_text(self):

		f = open("output.txt", "w")
		s = f.write(self.s)
		f.close()

		return s

	def print_result(self):
		print ""
		print "\33[92mConverted text\33[0m"
		print ""
		print self.s
		print ""




	def read_config(self):

		with open('config.yaml') as file:
			# The FullLoader parameter handles the conversion from YAML
			# scalar values to Python the dictionary format
			self.config_list = yaml.load(file, Loader=yaml.FullLoader)



	def proc_comments(self):

		count = 0
		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("\%")
			if(id1 == -1):
				break
			self.s = self.s[0:(id1)]+"pc"+self.s[(id1+2):]

		count = 0
		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("%")
			id2 = self.s.find("\n",id1+1)+1
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+"\n"+self.s[id2:]



	"""
	def proc_comments(self):

		print "len: ", len(self.s)

		count = 0
		base = 0
		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("%", base)
			base = id1
			id2 = self.s.find("\n",id1+1)+1
			if(id1 == -1):
				break
			if(self.s[id1-1] == "\\"):
				print "a"
				self.s = self.s[0:(id1-1)]+self.s[id1:]
			else:
				print "b"
				self.s = self.s[0:id1]+"\n"+self.s[id2:]
			print "base: ", base

			print "len: ", len(self.s)
	"""


	def proc_equation_on_text(self):

		#Remove equation
		count = 0
		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("$")
			id2 = self.s.find("$",id1+1)+1
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+str(chr(self.letters_number))+self.s[id2:]
			self.letters_number = self.letters_number + 1
			if(self.letters_number == 73):
				self.letters_number = self.letters_number + 1 #skip letter I
			if(self.letters_number == 91):
				self.letters_number = 66 #restart from letter B


	def proc_citations(self):
		count = 0
		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("\\cite{")
			id2 = self.s.find("}",id1+1)+1
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+"["+str(self.citations_number)+"]"+self.s[id2:]
			self.citations_number = self.citations_number + 1

		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("\\citep{")
			id2 = self.s.find("}",id1+1)+1
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+"["+str(self.citations_number)+"]"+self.s[id2:]
			self.citations_number = self.citations_number + 1

		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("\\citet{")
			id2 = self.s.find("}",id1+1)+1
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+"["+str(self.citations_number)+"]"+self.s[id2:]
			self.citations_number = self.citations_number + 1


	def proc_refs(self):
		count = 0
		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("\\ref{")
			id2 = self.s.find("}",id1+1)+1
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+str(self.references_number)+self.s[id2:]
			self.references_number = self.references_number + 1

		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("\\eqref{")
			id2 = self.s.find("}",id1+1)+1
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+"("+str(self.references_number)+")"+self.s[id2:]
			self.references_number = self.references_number + 1



	def proc_blanc_lines(self):
		count = 0
		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("\n\n\n")
			id2 = id1+3
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+"\n\n"+self.s[id2:]



	def proc_extra_spaces(self):
		count = 0
		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("  ")
			id2 = id1+1
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+self.s[id2:]

		count = 0
		while (count < MAX_FOR):
			count = count + 1
			id1 = self.s.find("\n ")
			id2 = id1+2
			if(id1 == -1):
				break
			self.s = self.s[0:id1]+"\n"+self.s[id2:]






	def proc_cmd_type_1(self):

		for cmd_str in self.config_list['type_1']:
			shift = len(cmd_str)+2
			base = 0
			count = 0
			while (count < MAX_FOR):
				count = count + 1
				id1 = self.s.find("\\"+cmd_str+"{",base)
				base = id1+1
				id2 = self.s.find("}",id1+1)+1
				if(id1 == -1):
					break
				if(self.s.find("{",id1+shift)!=-1):
					if(not (self.s.find("{",id1+shift)<id2)):
						self.s = self.s[0:id1]+self.s[(id1+shift):(id2-1)]+self.s[id2:]
				else:
					self.s = self.s[0:id1]+self.s[(id1+shift):(id2-1)]+self.s[id2:]




	def proc_cmd_type_2(self):

		for cmd_str in self.config_list['type_2']:
			shift = len(cmd_str)+2
			base = 0
			count = 0
			while (count < MAX_FOR):
				count = count + 1
				id1 = self.s.find("\\"+cmd_str+"{",base)
				base = id1+1
				id2 = self.s.find("}",id1+1)+1
				if(id1 == -1):
					break
				if(self.s.find("{",id1+shift)!=-1):
					if(not (self.s.find("{",id1+shift)<id2)):
						self.s = self.s[0:id1]+self.s[id2:]
				else:
					self.s = self.s[0:id1]+self.s[id2:]



	def proc_cmd_type_3(self):

		for cmd_str in self.config_list['type_3']:
			shift = len(cmd_str)+2
			base = 0
			count = 0
			while (count < MAX_FOR):
				count = count + 1
				id1 = self.s.find("\\"+cmd_str+"{",base)
				base = id1+1
				id2 = self.s.find("{",id1+shift)+1
				id3 = self.s.find("}",id2)+1
				if(id1 == -1):
					break
				if(self.s.find("{",id2+1)!=-1):
					if(not (self.s.find("{",id2+1)<id3)):
						self.s = self.s[0:id1]+self.s[(id2):(id3-1)]+self.s[id3:]
				else:
					self.s = self.s[0:id1]+self.s[(id2):(id3-1)]+self.s[id3:]




	def proc_cmd_type_4(self):

		for cmd_str in self.config_list['type_4']:
			shift = len(cmd_str)+2
			count = 0
			while (count < MAX_FOR):
				count = count + 1
				id1 = self.s.find("\\"+cmd_str)
				id2 = id1+shift
				if(id1 == -1):
					break
				self.s = self.s[0:id1]+self.s[id2:]


	def proc_cmd_type_5(self):

		for cmd_str in self.config_list['type_5']:
			shift = len(cmd_str)
			count = 0
			while (count < MAX_FOR):
				count = count + 1
				id1 = self.s.find("\\begin{"+cmd_str+"}")
				id2 = self.s.find("\\end{"+cmd_str+"}")
				if(id1 == -1):
					break
				self.s = self.s[0:id1]+self.s[(id2+shift+6):]




	def proc_cmd_type_6(self):

		for cmd_str in self.config_list['type_6']:
			shift = len(cmd_str)
			count = 0
			while (count < MAX_FOR):
				count = count + 1
				id1 = self.s.find("\\begin{"+cmd_str+"}")
				id2 = self.s.find("\\end{"+cmd_str+"}")
				if(id1 == -1):
					break
				self.s = self.s[0:id1]+self.s[(id1+shift+8):(id2-1)]+self.s[(id2+shift+6):]




	def proc_residues(self):

		for cmd_str in self.config_list['residues']:
			shift = len(cmd_str)
			base = 0
			count = 0
			while (count < MAX_FOR):

				count = count + 1
				id1 = self.s.find(cmd_str,base)
				id2 = id1 + shift
				base = id1+1
				if(id1 == -1):
					break
				self.s = self.s[0:id1]+"\33[41m"+self.s[id1:id2]+"\33[0m"+self.s[id2:]
				base = base + 5


def main():

	X = converter()

	X.proc_comments()

	X.proc_equation_on_text()

	X.proc_citations()

	X.proc_refs()


	for k in range(X.config_list['recursive_attempts']):
		X.proc_cmd_type_1()

		X.proc_cmd_type_2()

		X.proc_cmd_type_3()

	X.proc_cmd_type_4()

	X.proc_cmd_type_5()

	X.proc_cmd_type_6()


	X.proc_blanc_lines()
	X.proc_extra_spaces()


	X.write_output_text()

	X.proc_residues()

	X.print_result()


# Main
if __name__ == '__main__':


	main()



# ----------  ----------  ----------  ----------  ----------
