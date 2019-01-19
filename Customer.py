Apples = ["Customer1", "Customer3"]
Grapes = ["Customer2","Customer5","Customer6"]
Watermelons = ["Cusomer4","Customer7"]
A = len(Apples)
G = len(Grapes)
W = len(Watermelons)
Customer1 = "15 Apples"
Customer2 = "20 Grapes"
Customer3 = "25 Apples"
Customer4 = "5 Watermelons"
Customer5 = "10 Grapes"
Customer6 = "40 Grapes"
Customer7 = "10 Watermelons"
resp = ["Clients","clients"]
resp2 = ["Fruits","fruits"]
answer = input("What are you looking for? ")

if answer in resp:
    q1 = input("Which Client are you looking for? ")
    if q1 == "Customer 1":
        print(Customer1)
    else:
        pass
    if q1 == "Customer 2":
        print(Customer2)
    else:
        pass
    if q1 == "Customer 3":
        print(Customer3)
    else:
        pass
    if q1 == "Customer 4":
        print (Customer4)
    else:
        pass
    if q1 == "Customer 5":
        print(Customer5)
    else:
        pass
    if q1 == "Customer 6":
        print(Customer6)
    else:
        pass
    if q1 == "Customer 7":
        print(Customer7)
else:
    pass
if answer in resp2:
    q2 = input("Which product are you looking for? (Apples,Grapes,Watermelons) ")
    if q2 == "Apples":
        print(A)
    else:
        pass
    if q2 == "Grapes":
        print(G)
    else:
        pass
    if q2 == "Watermelons":
        print(W)
    else:
        pass
