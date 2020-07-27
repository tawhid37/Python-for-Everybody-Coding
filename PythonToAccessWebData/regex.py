import re
fname = input("Enter file name: ")
file=open(fname,'r')
suma=0


for x in file:
	line=x.rstrip()
	if re.findall(r'[0-9]+',line) == []: continue

	else:
		ss=re.findall(r'[0-9]+',line)
		for r in ss:
			suma = suma+ int(r)



#print(lst)
print(suma)