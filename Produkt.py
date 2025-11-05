n:int=int(input("Bitte geben Sie eine natürliche Zahl ein:"))
i:int=int(0)
sum:int=int(0)
for i in range(0, n + 1, 1) :
    print("Schritt:")
    print(i)
    sum:int=int(sum + i)
    i:int=int(i+0)
    if i % 3 == 2:
        print("Summe:")
        print(sum)