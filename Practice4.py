
# OOPs

# syntax for method



# create class , methods inside a class and call them using object

class FirstClass(): # syntax of class

    numb1 = 100 # class variable

    numb2 = 50

    def __init__(self): # constructor definition

        print("i'm called automatically !!!")

        print("i'm called first bfr other methods")

    # constructor --

    # nothing but a method

    # name of constructor is __init__

    # is called whenever is an obj of class is created. and constructor is called first ...

    def sample_method(self):

        print("hello world!!!")

        print("hru team!!")

    def sub(self, a, b):

        c = a- b

        print("sub of two no.: ", c)

    def sub(self, a, b):
        return a - b

    def add(self):
        return self.numb1 + self.numb2

    def inside_method(self):
        print(self.sub(10, 2))

    def multiply(self,a,b):
        return a*b

    def inside_method_multiply(self):
        print(self.multiply(self.numb1,self.numb2))


# calling methods by ojb

ob1 = FirstClass()  # create obj for a class

print(ob1.sub(30, 20))

ob1.sample_method()

print(ob1.numb1)

r1 = ob1.add()

print("sum of two class variables:", r1)

ob1.inside_method()

print("*******************")

ob2 = FirstClass()

result = ob2.sub(5, 1)

print(result)

print(ob2.multiply(5,6))

ob2.inside_method_multiply()

# assignment --> create a method to multiply two numbers

