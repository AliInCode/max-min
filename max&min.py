a = int(input("Enter Number 1 :"))
b = int(input("Enter Number 2 :"))
c = int(input("Enter Number 3 :"))
print(a , b , c )

if a > b and a > c :
    max = a
    print( f"max is : {max} ")
elif b > a and b > a :
    max = b
    print( f"max is : {max} ")
else:
    max = c
    print( f"max is : {max} ")
if a < b and a < c :
    min = a
    print( f"min is : {min} ")
elif b < a and b < a :
    min = b
    print( f"min is : {min} ")
else:
    min = c
    print( f"min is : {min} ")