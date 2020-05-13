"""Given a sequence originalSeq and an array of sequences, write a method to
find if originalSeq can be uniquely reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only
sequence such that all sequences in the array are subsequences of it.

Example 1:
Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
Output: true
Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct
[1, 2, 3, 4], in other words, all the given sequences uniquely define the order of numbers
in the 'originalSeq'.

Example 2:
Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
Output: false
Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely reconstruct
[1, 2, 3, 4]. There are two possible sequences we can construct from the given sequences:
1) [1, 2, 3, 4]
2) [1, 2, 4, 3]

Example 3:
Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
Output: true
Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct
[3, 1, 4, 2, 5].
"""
from collections import defaultdict, deque

"""
Time complexity # In step ‘d’, each number can become a source only once 
and each edge (a rule) will be accessed and removed once. Therefore, the time 
complexity of the above algorithm will be O(V+E)O(V+E), where ‘V’ is the 
count of distinct numbers and ‘E’ is the total number of the rules. Since, 
at most, each pair of numbers can give us one rule, we can conclude that the 
upper bound for the rules is O(N) where ‘N’ is the count of numbers in 
all sequences. So, we can say that the time complexity of our algorithm is 
O(V+N). 

Space complexity # The space complexity will be O(V+N), O(V+N), since we are 
storing all of the rules for each number in an adjacency list. 
"""


def can_construct(original_seq: list, sequences: list) -> bool:
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i - 1], sequence[i]
            graph[parent].append(child)
            in_degree[child] += 1
            in_degree.setdefault(parent, 0)

    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    order = []
    while queue:
        if len(queue) > 1:
            return False
        elif original_seq[len(order)] != queue[0]:
            return False

        node = queue.popleft()
        order.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return len(order) == len(original_seq)


def main():
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
