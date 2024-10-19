# Задание 3
# Создайте базовый класс Shape для рисования плоских
# фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами
# этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о
# каждой из фигур.

import json

class Shape:
    def show(self):
        pass

    def save(self, filename):
        with open(filename, 'a') as file:
            json.dump(self.__dict__, file)
            file.write('\n')  # Для разделения объектов

    @classmethod
    def load(cls, filename):
        shapes = []
        with open(filename, 'r') as file:
            for line in file:
                data = json.loads(line)
                shape_type = data.pop('type')
                if shape_type == 'Square':
                    shape = Square(**data)
                elif shape_type == 'Rectangle':
                    shape = Rectangle(**data)
                elif shape_type == 'Circle':
                    shape = Circle(**data)
                elif shape_type == 'Ellipse':
                    shape = Ellipse(**data)
                shapes.append(shape)
        return shapes

class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length
        self.type = 'Square'

    def show(self):
        print(f"Квадрат с координатами левого верхнего угла ({self.x}, {self.y}) и длиной стороны {self.side_length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = 'Rectangle'

    def show(self):
        print(f"Прямоугольник с координатами левого верхнего угла ({self.x}, {self.y}), шириной {self.width} и высотой {self.height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.type = 'Circle'

    def show(self):
        print(f"Окружность с центром ({self.x}, {self.y}) и радиусом {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = 'Ellipse'

    def show(self):
        print(f"Эллипс с координатами верхнего левого угла ({self.x}, {self.y}) и размерами {self.width}x{self.height}")

shapes = [
    Square(-1, -1, 5),
    Rectangle(1, 1, 10, 4),
    Circle(3, 0, 7),
    Ellipse(5, 6, 8, 4)
]

filename = 'shapes.txt'
for shape in shapes:
    shape.save(filename)

loaded_shapes = Shape.load(filename)

# Вывод информации о каждой загруженной фигуре
for shape in loaded_shapes:
    shape.show()