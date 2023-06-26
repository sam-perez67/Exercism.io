def equilateral(sides):
    a, b, c = sorted(sides)
    is_triangle = (a + b >= c) and (b + c >= a) and (a + c >= b) and a * b * c != 0
    return a == b == c and is_triangle


def isosceles(sides):
    a, b, c = sorted(sides)
    is_triangle = (a + b >= c) and (b + c >= a) and (a + c >= b) and a * b * c != 0
    return is_triangle and (a == b or b == c or c == a) 

def scalene(sides):
    a, b, c = sorted(sides)
    is_triangle = (a + b >= c) and (b + c >= a) and (a + c >= b) and a * b * c != 0
    return is_triangle and a != b != c != a
