




f = open("input.txt", "r")
s0 = f.read()
s = s0
# print(s)

MAX_FOR = 50

# print(type(s))

letters_number = 65

#Remove equation
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("$")
	id2 = s.find("$",id1+1)+1
	if(id1 == -1):
		break
	s = s[0:id1]+str(chr(letters_number))+s[id2:]
	letters_number = letters_number + 1
	if(letters_number == 73):
		letters_number = letters_number + 1
	if(letters_number == 91):
		letters_number = 65
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much $$\33[0m"



#Remove ref
number = 1
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\ref{")
	id2 = s.find("}",id1+1)+1
	# print id1, id2
	if(id1 == -1):
		break
	s = s[0:id1]+str(number)+s[id2:]
	# print s
	# print ""
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much ref{}\33[0m"


#Remove eqref
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\eqref{")
	id2 = s.find("}",id1+1)+1
	# print id1, id2
	if(id1 == -1):
		break
	s = s[0:id1]+"("+str(number)+")"+s[id2:]
	# print s
	# print ""
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much eqref{}\33[0m"


#Remove cite
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\cite{")
	id2 = s.find("}",id1+1)+1
	# print id1, id2
	if(id1 == -1):
		break
	s = s[0:id1]+"["+str(number)+"]"+s[id2:]
	# print s
	# print ""
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much cite{}\33[0m"




#Remove comments
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("%")
	id2 = s.find("\n",id1+1)+1
	# print id1, id2
	if(id1 == -1):
		break
	s = s[0:id1]+" "+s[id2:]
	# print s
	# print ""
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much comments\33[0m"


#Remove noindent
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\noindent")
	id2 = id1+10
	# print id1, id2
	if(id1 == -1):
		break
	s = s[0:id1]+s[id2:]
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much noindent\33[0m"


#Remove \QEDA and \QEDB
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\QED")
	id2 = id1+5
	# print id1, id2
	if(id1 == -1):
		break
	if(s[id1+4]=="A" or s[id1+4]=="B"):
		s = s[0:id1]+s[id2:]
		number = number + 1
if (count == 2):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much \\QED\33[0m"





#Remove \emph{
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\emph{")
	id2 = s.find("}",id1+1)+1
	if(id1 == -1):
		break
	s = s[0:id1]+s[(id1+6):(id2-1)]+s[id2:]
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much emph{}\33[0m"

#Remove \textit{
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\textit{")
	id2 = s.find("}",id1+1)+1
	if(id1 == -1):
		break
	s = s[0:id1]+s[(id1+6):(id2-1)]+s[id2:]
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much textit{}\33[0m"

"""
#Remove \rev{ - note, this is done after all
for attempts in range(3): #try 3 times to remove \rev inside \rev
	base = 0
	count = 0
	while (count < MAX_FOR):
		count = count + 1
		id1 = s.find("\\rev{",base)
		base = id1+1
		id2 = s.find("}",id1+1)+1
		if(id1 == -1):
			break
		if(s.find("{",id1+5)!=-1):
			if(not (s.find("{",id1+5)<id2)):
				s = s[0:id1]+s[(id1+5):(id2-1)]+s[id2:]
		else:
			s = s[0:id1]+s[(id1+5):(id2-1)]+s[id2:]
"""
#Remove \rev{ and \textcolor - note, this is done after all
for attempts in range(3): #try 3 times to remove \rev/\textcolor inside \rev/\texcolor
	#Remove a internal rev
	base = 0
	count = 0
	while (count < MAX_FOR):
		count = count + 1
		id1 = s.find("\\rev{",base)
		base = id1+1
		id2 = s.find("}",id1+1)+1
		if(id1 == -1):
			break
		if(s.find("{",id1+5)!=-1):
			if(not (s.find("{",id1+5)<id2)):
				s = s[0:id1]+s[(id1+5):(id2-1)]+s[id2:]
		else:
			s = s[0:id1]+s[(id1+5):(id2-1)]+s[id2:]

	#Remove a internal textcolor
	base = 0
	count = 0
	while (count < MAX_FOR):
		count = count + 1
		id1 = s.find("\\textcolor{",base)
		base = id1+1
		id2 = s.find("{",id1+11)+1 #close color
		id3 = s.find("}",id2+1)+1 #close text
		if(id1 == -1):
			break
		if(s.find("{",id2+1)!=-1):
			if(not (s.find("{",id2+1)<id3)):
				s = s[0:id1]+s[(id2):(id3-1)]+s[id3:]
		else:
			s = s[0:id1]+s[(id2):(id3-1)]+s[id3:]



#Remove \color{}
base = 0
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\color{",base)
	base = id1+1
	id2 = s.find("}",id1+1)+1
	if(id1 == -1):
		break
	s = s[0:id1]+s[id2:]
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much color{}\33[0m"

#Remove \section{}
base = 0
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\section{",base)
	base = id1+1
	id2 = s.find("}",id1+1)+1
	if(id1 == -1):
		break
	s = s[0:id1]+s[id2:]
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much section{}\33[0m"

#Remove \subsection{}
base = 0
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\subsection{",base)
	base = id1+1
	id2 = s.find("}",id1+1)+1
	if(id1 == -1):
		break
	s = s[0:id1]+s[id2:]
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much section{}\33[0m"

#Remove \label{}
base = 0
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\\label{",base)
	base = id1+1
	id2 = s.find("}",id1+1)+1
	if(id1 == -1):
		break
	s = s[0:id1]+s[id2:]
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much label{}\33[0m"





#Remove extra spaces
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("  ")
	id2 = id1+1
	if(id1 == -1):
		break
	s = s[0:id1]+s[id2:]
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much multiple spaces\33[0m"


#Remove extra \n
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\n\n\n")
	id2 = id1+3
	if(id1 == -1):
		break
	s = s[0:id1]+"\n\n"+s[id2:]
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much multiple \\n\33[0m"



#Remove extra \n + space
count = 0
while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("\n ")
	id2 = id1+2
	if(id1 == -1):
		break
	s = s[0:id1]+"\n"+s[id2:]
	number = number + 1
if (count == MAX_FOR):
	print "\n\33[31mCheck that result !\33[0m"
	print "\n\33[31mToo much multiple \\n+space\33[0m"




#####################


if (not (s.find("\\rev{") == -1)):
	base = 0
	while (count < MAX_FOR):
		count = count + 1
		id1 = s.find("\\rev{",base)
		id2 = id1 + 5
		base = id1+1
		if(id1 == -1):
			break
		s = s[0:id1]+"\33[31m"+s[id1:id2]+"\33[0m"+s[id2:]
		base = base + 7

while (count < MAX_FOR):
	count = count + 1
	id1 = s.find("}",base)
	id2 = id1 + 1
	base = id1+1
	if(id1 == -1):
		break
	s = s[0:id1]+"\33[31m"+s[id1:id2]+"\33[0m"+s[id2:]
	base = base + 1


print ""
print "\33[93mOriginal text\33[0m"
print ""
print s0
print ""
print ""
print "\33[92mCompiled text\33[0m"
print ""
print s


if (not (s.find("\\rev{") == -1)):
	print "\33[91mFound \\rev{} command !\33[0m"
	print ""
#Warnning - textcolor
if (not (s.find("\\textcolor{") == -1)):
	print "\33[91mFound \\textcolor{} command !\33[0m"
	print ""
print ""

f.close()

f = open("output.txt", "w")
f.write(s)
f.close()






