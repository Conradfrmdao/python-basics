class Myclass:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        print(f"{a}, {b}, {c} are initialized in the class Myclass")
o1= Myclass(1, 2, 3)  # Creates an instance of Myclass with parameters 1, 2, and 3
print(o1.a, o1.b, o1.c)  # Accesses the attributes
