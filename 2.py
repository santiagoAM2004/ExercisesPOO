class Square():
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        squarePerimeter = self.side * 4
        return squarePerimeter

    def surface(self):
        squarePerimeter = self.side * 2
        return squarePerimeter

square1 = Square(5)
square2 = square1
print(f"Perimeter: {square2.perimeter()}, Surface: {square2.surface()}")



