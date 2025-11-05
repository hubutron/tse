n:int=int(input("Bitte geben Sie eine natürliche Zahl ein:"))
i:int=int(0)
for i in range(n, -1, -1) :
    if i % 2 == 0:
        print(i)