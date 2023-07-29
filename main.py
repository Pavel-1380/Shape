class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


# класс отрезок
class Segment:

    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def get_len(self):
        return ((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2) ** 0.5


def check_intersection(point1: tuple, point2: tuple, point3: tuple, point4: tuple):
    # проверка на наличие пересечения и нахождение общей точки отрезков
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    x4, y4 = point4
    if x1 >= x2:
        x1, x2 = x2, x1
    if x3 >= x4:
        x3, x4 = x4, x3
    if x1 <= x2 and x3 <= x4:
        if (x1 <= x4 and x4 <= x2) or (x1 <= x3 and x3 <= x2):
            print('Отрезки имеют точку пересечения')
        else:
            print('У отрезков нет общей точки')
            return
    if y2 == y1:
        k1 = 0
    else:
        k1 = (y2 - y1) / (x2 - x1)
    if y3 == y4:
        k2 = 0
    else:
        k2 = (y4 - y3) / (x4 - x3)
    if k1 == k2:
        print('Отрезки параллельны, т.к. угловой коэффициент равен')

    d1 = y1 - k1 * x1
    d2 = y3 - k2 * x3

    x = round((d2 - d1) / (k1 - k2), 2)
    y = round((k1 * x + d1), 2)

    print(f'Точка пересечения отрезков x = {x}, y = {y}')
    return x, y


class Triangle:

    def __init__(self, point1, point2, point3) -> None:
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.a = Segment(self.point1, self.point2).get_len()
        self.b = Segment(self.point2, self.point3).get_len()
        self.c = Segment(self.point3, self.point1).get_len()

    def get_len_median(self):
        # возвращает длину медианы
        return round((((2 * self.a ** 2 + 2 * self.b ** 2 - self.c ** 2) ** 0.5) / 2), 2)

    def get_perimeter(self):
        # возвращает периметр
        return round((self.a + self.b + self.c), 2)

    def get_square(self):
        # возвращает площадь
        self.p = self.get_perimeter() / 2
        self.s = (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5
        print(f'площадь треугольника 1 равна {round((self.s), 2)}')
        return round(self.s, 2)

    def check_angle(self):
        # проверка на угол (тупой, прямой или острый) по теореме Пифагора,
        # если угол прямой, она должна выполняться
        sorted_sides = sorted([self.a, self.b, self.c])
        hypotenuse = sorted_sides[-1]
        katet1 = sorted_sides[0]
        katet2 = sorted_sides[1]
        if hypotenuse ** 2 == katet1 ** 2 + katet2 ** 2:
            print('Треугольник прямоугольный')
        if hypotenuse ** 2 > katet1 ** 2 + katet2 ** 2:
            print('Треугольник тупоугольный')
        if hypotenuse ** 2 < katet1 ** 2 + katet2 ** 2:
            print('Углы острые')

    def check_segment_for_triangle(self):
        # проверка на возможность построения треугольника из отрезков следующей длины
        if self.a + self.b > self.c:
            if self.a + self.c > self.b:
                if self.b + self.c > self.a:
                    return True
                return False
            return False
        return False


class Tetragon(Triangle):

    def __init__(self, point1, point2, point3, point4) -> None:
        super().__init__(point1, point2, point3)
        self.point4 = point4
        self.a = Segment(self.point1, self.point2).get_len()
        self.b = Segment(self.point2, self.point3).get_len()
        self.c = Segment(self.point3, self.point1).get_len()
        self.d = Segment(self.point3, self.point4).get_len()
        self.e = Segment(self.point4, self.point1).get_len()

    def get_perimeter(self):
        # из метода суперкласса минусуем сторону c и добавляем d и e
        return round((super().get_perimeter() - self.c + self.d + self.e), 2)

    def get_square(self):
        # возвращает площадь, как сумму двух треугольников
        p1 = (self.a + self.b + self.c) / 2
        p2 = (self.c + self.d + self.e) / 2
        s1 = (p1 * (p1 - self.a) * (p1 - self.b) * (p1 - self.c)) ** 0.5
        s2 = (p2 * (p2 - self.c) * (p2 - self.d) * (p2 - self.e)) ** 0.5
        return round((s1 + s2), 2)

    def convexity_check(self):
        # проверка на выпуклость
        t1 = ((self.point4.x - self.point1.x) * (self.point2.y - self.point1.y) - (self.point4.y - self.point1.y) * (
                self.point2.x - self.point1.x))
        t2 = ((self.point4.x - self.point2.x) * (self.point3.y - self.point2.y) - (self.point4.y - self.point2.y) * (
                self.point3.x - self.point2.x))
        t3 = ((self.point4.x - self.point3.x) * (self.point1.y - self.point3.y) - (self.point4.y - self.point3.y) * (
                self.point1.x - self.point3.x))
        t4 = ((self.point1.x - self.point3.x) * (self.point2.y - self.point3.y) - (self.point1.y - self.point3.y) * (
                self.point2.x - self.point3.x))
        return t1 * t2 * t3 * t4 > 0


if __name__ == '__main__':
    A = Point(0, 0)
    B = Point(0, 9)
    C = Point(9, 9)
    D = Point(9, 0)

    s1 = Segment(A, B)
    print(s1.get_len())
    tr1 = Triangle(A, B, C)
    tr1.check_angle()
    print(tr1.get_len_median())
    print(tr1.check_segment_for_triangle())
    print(tr1.get_perimeter())
    print(tr1.get_square())
    tetragon1 = Tetragon(A, B, C, D)
    print(tetragon1.get_perimeter())
    print(tetragon1.get_square())
    # проверка на выпуклость
    print(tetragon1.convexity_check())
    tetragon2 = Tetragon(Point(0, 2), Point(1, 7), Point(7, 6), Point(1, 9))
    print(tetragon2.get_square())
    print(tetragon2.get_perimeter())
    check_intersection((1, 1), (7, 8), (1, 7), (8, 1))
