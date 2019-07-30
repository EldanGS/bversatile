"""
Matrix N x N, position coordinate (start.x, start.y), short path to destination
Matrix is integer value. (1 is destination) (0 path)
O(1) space, O(time) as fast as possible
"""

bikes_location = {(1, 4), (3, 2)}


def is_bike(x, y):
    return (x, y) in bikes_location


def find_closest_bike(start_x, start_y) -> tuple:
    if is_bike(start_x, start_y):
        return (start_x, start_y)

    dist = 1
    while True:
        right_up_x, right_up_y = start_x - dist, start_y + dist
        right_down_x, right_down_y = start_x + dist, start_y + dist
        left_up_x, left_up_y = start_x - dist, start_y - dist
        left_down_x, left_down_y = start_x + dist, start_y - dist

        x, y = start_x - dist, start_y

        while x <= right_up_x and y < right_down_y:
            if is_bike(x, y):
                return (x, y)
            y += 1

        while x < right_down_x and y <= right_down_y:
            if is_bike(x, y):
                return (x, y)
            x += 1

        while x <= left_down_x and y > left_down_y:
            if is_bike(x, y):
                return (x, y)
            y -= 1

        while x > left_up_x and y >= left_up_y:
            if is_bike(x, y):
                return (x, y)
            x -= 1

        while x <= start_x - dist and y < start_y:
            if is_bike(x, y):
                return (x, y)
            y += 1

        dist += 1
        if dist > 10:
            break

    return (-1, -1)


if __name__ == '__main__':
    start_x, start_y = 1, 3

    expected = (1, 4)
    actual = find_closest_bike(start_x, start_y)

    assert actual == expected, 'Incorrect'
    print('Correct', actual)
