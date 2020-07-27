
fname = input("Enter file name: ")

file=open(fname,'r')

for x in file:
    x = x.rstrip()
    print(x.upper())

