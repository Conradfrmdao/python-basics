class conrad:
    a=100
    def func(self):
        print("This is a function in the class conrad")


obj=conrad()
obj.func()  # Calls the function defined in the class
print(obj.a)  # Accesses the class variable 'a'

class car:
    def bmw(self,color,type,engine):
        print(f"This is a {color} {type} with a {engine} engine.")

car=car()
car.bmw("red", "M4 Competition", "V8")  # Calls the method in the class car

