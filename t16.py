def is_point_inside_triangle(x1, y1, x2, y2, x3, y3, x, y):
    # Барицентрические координаты
    denominator = ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    alpha = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denominator
    beta = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denominator
    gamma = 1 - alpha - beta

    # Проверка условия лежания точки внутри треугольника
    if 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1:
        return True
    else:
        return False


def test_is_point_inside_triangle():
    print(is_point_inside_triangle(0, 0, 4, 0, 2, 4, 2, 2) == True)
    print(is_point_inside_triangle(0, 0, 4, 0, 2, 4, 2, 0) == True)
    print(is_point_inside_triangle(0, 0, 4, 0, 2, 4, 5, 5) == False)


test_is_point_inside_triangle()