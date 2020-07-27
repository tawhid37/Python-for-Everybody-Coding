
def computepay(hr,rph):
    if hr==40:
        pay=40*rps
        return pay
    elif hr>40:
        extra=hr-40
        pay= rph*1.5*extra+(40*rph)
        return pay
    else:
        pay=0
        return pay

hrs = input("Enter Hours:")
hr = float(hrs)
rate=input("Enter Rate per hour:")
rph = float(rate)

pay= computepay(hr,rph)
print('Pay',pay)
