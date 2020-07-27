fname = input("Enter file name: ")
file=open(fname,'r')

lst=list()

for x in file:
	line=x.rstrip()
	words = line.split()

	for word in words:
		#print(word)
		if word not in lst:
			lst.append(word)


lst.sort()
print(lst)
	



