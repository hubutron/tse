import sys

print("Hello World!")
a:int=int(sys.argv[1])
b:int=int(sys.argv[2])
if b>a :
    print("b ist: %d und somit größer als a, welches den Wert %d beträgt"  % (b, a))
else :
    print("a ist: %d und somit größer als b, welches den Wert %d beträgt" % (a, b))