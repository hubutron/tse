n:int=int(input("Bitte geben Sie eine natürliche Zahl ein:"))
i:int=int(1)
p:int=int(1)
print(i)
print("*")
while i<n :
    print(i)
    print("Ergebnis:")
    p:int=int(p*i)
    print(p)
    i:int=int(i+1)
    if i<n :
        print("*")