def rectangle_intersection(rect1, rect2):
    # ищем правый верхний угол
    x1 = max(rect1[0][0], rect2[0][0])
    y1 = min(rect1[0][1], rect2[0][1])

    # ищем левый нижний угол
    x2 = min(rect1[1][0], rect2[1][0])
    y2 = max(rect1[1][1], rect2[1][1])

    # Не пересекаются
    if y2 > y1 or x1 > x2:
        return 0

    # модуль числа позволяет учитывать разное положение прямоугольников относительно друг друга
    return abs(x2 - x1) * abs(y2 - y1)


def test_rectangle_intersection():
    print(rectangle_intersection([[-4, 7], [2, -2]], [[-1, 2], [6, -7]]) == 12)
    print(rectangle_intersection([[-5, 5], [1, -1]], [[-7, 7], [3, -3]]) == 36)
    print(rectangle_intersection([[10, 10], [1, 1]], [[-5, -5], [-15, -15]]) == 0)


test_rectangle_intersection()



