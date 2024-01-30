from rectangle import Rectangle, Square, Circle


# Создаем два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# Выводим площадь наших двух прямоугольников

print(rect_1.getArea())
print(rect_2.getArea())

# Выводим квадрат одной из сторон

square_1 = Square(5)
square_2 = Square(10)

print(square_1.getAreaSquare(),
      square_2.getAreaSquare())

print("====================================")

figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.getAreaSquare())
    else:
        print(figure.getArea())

circle_1 = Circle(5)
circle_2 = Circle(25)

print(circle_1.getAreaCircle(),
      circle_2.getAreaCircle())