
fname = input("Enter file name: ")
count=0
total=0.0
file=open(fname,'r')

for x in file:
    if x.startswith("X-DSPAM-Confidence:") :
    	#print(x)
    	x=x.rstrip()
    	count=count+1
    	pos=x.find(':')
    	num=float(x[pos+2:])
    	total= total+num

    	#print(x[pos+2:])
   
print("Average spam confidence:",round(total/count, 12))
