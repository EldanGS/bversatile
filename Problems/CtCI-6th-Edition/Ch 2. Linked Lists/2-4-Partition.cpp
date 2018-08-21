/*
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. 
lf x is contained within the list, the values of x only need to be after the elements less than x (see below).
The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
Cracking the Coding Interview, 6th Edition
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 ->10 -> 2 -> 1[partition=5) 
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
*/

#include "listConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

/*
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
*/
ListNode * Partition(ListNode * head, int x) {
    ListNode node1(0), node2(0);
    ListNode *ptr1 = &node1, *ptr2 = &node2;

    while (head) {
        if (head -> val < x) {
            ptr1 = ptr1 -> next = head;
        } else {
            ptr2 = ptr2 -> next = head;
        }

        head = head -> next;
    }

    ptr2 -> next = NULL;
    ptr1 -> next = node2.next;

    return node1.next;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    ListNode * head = NULL;
    for (int i = 10; i >= 1; i--) {
        insert(head, random_range(1, 9));
    }

    printList(head);
    printList(random_range(head, 5));


    return 0;
}
