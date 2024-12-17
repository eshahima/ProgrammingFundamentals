#class is a template to create new objects
#functions is a set of code that is run when its called; it can have parameters and return data
        #init function: a built in function when class is intiated; used to assign values to object properties
class Circle: 
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * int(self.radius) * int(self.radius)

class Rectangle: 
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return int(self.width) * int(self.height)

#make sure classes always come first


userinput = input("Do you want to calculate area for circle or rectangle?")
if userinput.lower() == 'circle':
    radius = input("Enter radius of circle:")
    circle = Circle(radius)
    print(circle.area())

elif userinput.lower() == 'rectangle':
    height = input("Enter height of rectangle:")
    width = input("Enter width of rectangle:")
    rectangle = Rectangle(height, width)
    print(rectangle.area())

else:
   print("Enter either circle or rectangle")
 

