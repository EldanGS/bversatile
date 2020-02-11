"""
Given a submarines with certain amount of air in it, and number of people to seat in submarines.
All submarines sorted by amount of air in descending order.

The question is, distribute people on the submarines so that everyone
has as maximum air as possible.

Example,
input: submarines = [10, 6, 2, 1], people = 6
output: [4, 2, 0, 0]
explanation: For first submarine we put 4 people and each of them has 10 / 4 = 2.5 amount of air,
to the second submarine distributed 2 people and they are has 6 / 2 = 3.0 amount of air.

"""
import heapq


def get_people(submarines, mid):
    return sum(air // mid for air in submarines)


def max_air_for_people_in_submarines(submarines: list, people: int) -> list:
    if not submarines or not people:
        return []

    result = [0] * len(submarines)
    left, right = 0, sum(submarines)

    for _ in range(60):
        mid = (left + right) / 2
        cur_people = get_people(submarines, mid)

        if cur_people >= people:
            left = mid
        else:
            right = mid

    min_air = left
    for i, air in enumerate(submarines):
        join = int(air // min_air)
        result[i] = min(people, join)
        people -= min(people, join)

    return result


class Submarine:

    def __init__(self, air: int, count: int, index: int):
        self.air = air
        self.count = count
        self.index = index

    def __lt__(self, other):
        return self.air / self.count > other.air / other.count


def max_air_for_people_in_submarines2(submarines: list, people: int) -> list:
    n = len(submarines)
    heap = [Submarine(air, 1, i) for i, air in enumerate(submarines)]
    heapq.heapify(heap)
    result = [0] * n
    while people > 0:
        submarine = heapq.heappop(heap)
        result[submarine.index] += 1
        submarine.count += 1
        heapq.heappush(heap, submarine)
        people -= 1

    return result


if __name__ == '__main__':
    submarines = [10, 6, 4, 1]
    people = 7
    print(max_air_for_people_in_submarines(submarines, people))
    print(max_air_for_people_in_submarines2(submarines, people))
    submarines = [14, 11, 10, 6, 4, 1]
    people = 77
    print(max_air_for_people_in_submarines(submarines, people))
    print(max_air_for_people_in_submarines2(submarines, people))