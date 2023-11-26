hour = int(input("saat:"))
rate = int(input("hoghoogh saati:"))

def salary(time , money):
    t = time * money
    print("hoghoogh sabet : " , t)
    return t

def over_pay(time , money):
    payment = time * (money * 1.5)
    print("ezafe kari :" , payment)
    return time * (money * 1.5)


def regular(time , money):
    if time > 160 :
        a = over_pay(time , money)
        b = salary(time , money)
        print("hoghoogh kamel :" , a-b)
    else :
        c = salary(time , money)
        print("hoghoogh kamel:" , c , "ezafe kari : 0")

regular(hour , rate)