class Rectangle(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        for j in range(self.width):
          picture += "*"
        
        picture += "\n"
      
      return picture

  def get_amount_inside(self, shape):
    #self 4 x 8; shape = 4 x 4
    if shape.height <= self.height and shape.width <= self.width:
      return int(self.get_area() / shape.get_area())
    else:
      return 0

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, side):
    self.height = side
    self.width = side

  def set_width(self, side):
    self.set_side(side)

  def set_height(self, side):
    self.set_side(side)
