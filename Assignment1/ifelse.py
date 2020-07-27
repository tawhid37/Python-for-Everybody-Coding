hrs = input("Enter Hours:")
hr = float(hrs)
rate=input("Enter Rate per hour:")
rph = float(rate)
pay=0

if hr==40:
    pay=40*rps
elif hr>40:
    extra=hr-40
    pay= rph*1.5*extra+(40*rph)
else:
    pay=0
print(pay)
