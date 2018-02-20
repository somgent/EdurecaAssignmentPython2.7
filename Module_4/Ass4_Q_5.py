#Q5++++++++++++++++++ Calculate the area of a box++++++++++++++++++++

class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an instance of Box.
x = Box(5, 5)

# Print area.
print "Area of box 10x2 =", x.area()