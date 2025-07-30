class Myclass:
    def _init_(self, a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c
        print(f"{a}, {b}, {c} are initialized in the class Myclass")

obj = Myclass(2,3,4)  # Creates an instance of Myclass with parameters 1, 2, and 3
