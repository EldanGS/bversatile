from test_framework import generic_test
import collections


def flip_color(x, y, image):
    color = image[x][y]
    image[x][y] ^= 1
    queue = collections.deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x])
                    and image[next_x][next_y] == color):
                image[next_x][next_y] ^= 1
                queue.append((next_x, next_y))


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("18-02-matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
