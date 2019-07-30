# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2 or []

        result = []
        n, m = len(list1), len(list2)
        i, j = 0, 0
        start, end = list1[0].start, list1[0].end
        if start > list2[0].start:
            start, end = list2[0].start, list2[0].end

        while i < n and j < m:
            if i < n and end > list1[i].start:
                start = min(start, list1[i].start)
                end = max(end, list1[i].end)
                i += 1
            elif j < m and end > list2[j].start:
                start = min(start, list2[j].start)
                end = max(end, list2[j].end)
                j += 1
            else:
                result.append(Interval(start, end))

                start, end = list1[i].start, list1[j].end
                if start > list2[j].start:
                    start, end = list2[j].start, list2[j].end
                    j += 1
                else:
                    i += 1

        if i < n:
            result.extend(list1[i:])
        if j < m:
            result.extend(list2[j:])

        return result


if __name__ == '__main__':
    list1 = [Interval(1, 5), Interval(10, 14), Interval(16, 18)]
    list2 = [Interval(2,6), Interval(8,10), Interval(11,20)]

    solution = Solution()
    for interval in solution.mergeTwoInterval(list1, list2):
        print(interval.start, interval.end)

