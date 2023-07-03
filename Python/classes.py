# This line defines a class called Point. A class is like a blueprint for creating objects.
class Point():


    #This line defines a method called __init__. The __init__ method is called when an object of the Point class is created.
    def __init__(self,input1,input2):
        # This line assigns the value of input1 to the x property of the Point object
        self.x = input1
        # This line assigns the value of input2 to the y property of the Point object.
        self.y = input2

# This line creates an object of the Point class. The x property of this object is assigned the value of 2 and the y property is assigned the value of 8.
p = Point(2, 8)

# These lines print the values of the x and y properties of the p object. In this case, the output will be:
print(p.x)
print(p.y)