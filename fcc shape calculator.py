class Rectangle:
    def __init__(self, width, height):
        self.width= width
        self.height= height
    def __str__(self):
        return (("Rectangle(width={0}, height={1})").format(self.width, self.height))
    def set_width(self, width):
        self.width= width
    def set_height(self, height):
        self.height= height
    def get_area(self):
        return self.height * self.width
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 +self.height ** 2) **(1/2)
    def get_picture(self):
        if self.width<50 or self.height<50:
            for i in range(self.height):
                for j in range(self.width):
                    if j!=self.width -1 :
                        print("*", end="")
                    else:
                        print("*")
            return ""
        else:
            print("Too big for picture.")

    def get_amount_inside(self, Shape):

        return (self.get_area() // Shape.get_area())
class Square(Rectangle):
    def __init__(self, side):
        self.side= side
        self.height= side
        self.width= side

    def __str__(self):
        return (("Square(side={0})").format(self.side))
    def set_side(self, side):
        self.width=side
        self.height=side
        self.side=side
    def set_height(self, height):
        self.height=height
        self.width= height
    def set_width(self, width):
        self.width=width
        self.height=width
rect =Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
sq =Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
print(rect.get_picture())