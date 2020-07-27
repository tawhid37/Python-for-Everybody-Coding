largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        val=float(num)
    except:
        print('Invalid input')
        continue

    if smallest is None:
        smallest=val
    #print("First smallest:",smallest)
    if largest is None:
        largest=val
    #print("First largest:",largest)

    if val > largest:
        #print("In largest",val)
        largest=val

    if val < smallest:
        #print("In smallest",val)
        smallest=val



print("Maximum is", int(largest))
print("Minimum is", int(smallest))
