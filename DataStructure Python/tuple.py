fname = input("Enter file name: ")
file=open(fname,'r')
count=dict()
lst=list()
er=None

for x in file:
	line=x.rstrip()
	if line.startswith('From '):
		words=line.split()
		x=words[5].split(':')
		lst.append(x[0])


for nm in lst:
	count[nm]= count.get(nm,0)+1


for k,v in sorted(count.items()):
	print(k,v)

