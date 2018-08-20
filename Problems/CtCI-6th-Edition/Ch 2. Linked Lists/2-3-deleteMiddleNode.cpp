#include "listConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

/*
Delete Middle Node: Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
*/

/*
If I have whole list;
1st solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
*/
void deleteMiddleNode_total(ListNode * head) {
    if (!head) {
        return;
    }

    if (!head -> next) {
        delete head;
        return;
    }
    
    ListNode * prev = NULL;
    ListNode * walker = head;
    ListNode * runner = head;

    while (runner and runner -> next) {
        runner = runner -> next -> next;
        prev = walker;
        walker = walker -> next;
    }

    prev -> next = walker -> next;
    delete walker;
}

/*
If I have only list;
2nd solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
*/
void deleteMiddleNode_point(ListNode * head) {
    if (!head) {
        return;
    }

    ListNode * nextNode = head -> next;
    head -> val = nextNode -> val;
    head -> next = nextNode -> next;
    delete nextNode;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    ListNode * head = NULL;
    for (int i = 10; i >= 1; i--) {
        insert(head, i);
    }

    printList(head);
    deleteMiddleNode_total(head);
    printList(head);


    return 0;
}