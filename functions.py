def add (a,b):
    print(a+b)
def multi (a,b):
    print(a*b)
def sub (a,b):
    print(a-b)
def div (a,b):
    if b != 0:
        print(a/b)
    else:
        print("Error! Division by zero.")

numb= float(input("Enter first number: "))
numb2= float(input("Enter second number: "))

add(numb, numb2)
multi(numb, numb2)
sub(numb, numb2)
div(numb, numb2)
print("End of calculations")
