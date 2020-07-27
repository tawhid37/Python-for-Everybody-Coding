fname = input("Enter file name: ")
file=open(fname,'r')
count=dict()
lst=list()
emailname=None
emailnumber=None

for x in file:
	line=x.rstrip()
	if line.startswith('From '):
		words=line.split()
		lst.append(words[1])

for email in lst:
	count[email]= count.get(email,0)+1


for email,count in count.items():
	if emailnumber is None or count > emailnumber:
		emailname= email
		emailnumber=count


print(emailname,emailnumber)
		

