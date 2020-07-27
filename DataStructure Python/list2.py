fname = input("Enter file name: ")
file=open(fname,'r')
count=0
lst=list()

for x in file:
	line=x.rstrip()
	if line.startswith('From '):
		words=line.split()
		count=count+1
		print(words[1])

print("There were", count, "lines in the file with From as the first word")


"""count = 0
for line in fh:
    line = line.rstrip()
    words=line.split()
    if len(words) == 0 : continue
    if words[0] !='From': continue
    email = words[1]
    print(email)
    if words[0] =='From':
       count+=1
print("There were", count, "lines in the file with From as the first word")
	"""


