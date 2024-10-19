# Задание 1
# Создать базовый класс Фигура с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади.

# Задание 2
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str (возвращает
# информацию о фигуре).
import math

class Figure:
    def area(self):
        pass

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return "Фигура"

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Прямоугольник: ширина = {self.width}, высота = {self.height}, площадь = {self.area()}"

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        return f"Круг: радиус = {self.radius}, площадь = {self.area():.2f}"

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
    def __str__(self):
        return f"Прямоугольный треугольник: основание = {self.base}, высота = {self.height}, площадь = {self.area()}"

class Trapeze(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height
    
    def __str__(self):
        return f"Трапеция: первое основание = {self.base1}, второе основание = {self.base2}, высота = {self.height}, площадь = {self.area()}"

rectangle = Rectangle(2, 5)
circle = Circle(3)
triangle = RightTriangle(6, 8)
trapeze = Trapeze(7, 8, 9)


print(f"Площадь прямоугольника: {rectangle.area()} кв. ед.")
print(f"Площадь круга: {circle.area():.2f} кв. ед.")
print(f"Площадь прямоугольного треугольника: {triangle.area()} кв. ед.")
print(f"Площадь трапеции: {trapeze.area()} кв. ед.")

print(f"Площадь прямоугольника как целое число: {int(rectangle)}")
print(f"Площадь круга как целое число: {int(circle)}")


