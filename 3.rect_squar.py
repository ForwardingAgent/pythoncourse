class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        # self.rect = rect()  # ('Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ")'")

    def __str__(self):
        if self.__class__ == Rectangle:
            return ('Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ")")
        else:
            return ('Square(side=' + str(self.width) + ')')

    def set_width(self, width):  # устанавливаем ширину
        self.width = width

    def set_height(self, height):  # устанавливаем длину
        self.height = height

    def get_area(self):  # площадь
        return self.width * self.height

    def get_perimeter(self):  # периметр
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):  # диагональ
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):  # рисуем
        if self.height > 50:
            return ('Too big for picture.')
        else:
            # for p in range(self.height - 1):
            #    print(('*' * self.width), end='\n')
            return ((('*' * self.width) + '\n') * self.height)

    def get_amount_inside(self, amount):
        if amount.__class__ == Rectangle:
            self.area = self.width * self.height
            amount.square = amount.height * amount.width
            return amount.square // self.area

        else:
            if amount.__class__ == Square:
                if amount.width > self.width:
                    return 0
                else:
                    self.area = self.width * self.height
                    self.square = amount.width ** 2
                    return self.area // self.square


class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = self.width
        # self.side = self.width

    def set_side(self, width):
        self.width = width
        self.height = self.width
        # self.width = self.height = self.side


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
rect2 = Rectangle(4, 4)
print(rect2.get_amount_inside(rect))

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))