#include "listConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);


/*
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
*/
Node * kthToLast_iter(Node * head, int k) {
    if (!head) {
        return head;
    }

    Node * ptr1 = head;
    Node * ptr2 = head;

    while (k-- and ptr1) {
        ptr1 = ptr1 -> next;
    }

    if (k > 0) {
        return NULL;
    }

    while (ptr1) {
        ptr1 = ptr1 -> next;
        ptr2 = ptr2 -> next;
    }

    return ptr2;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    Node * head = NULL;
    for (int i = 10; i >= 1; i--) {
        insert(head, i);
    }

    printList(head);
    printList(kthToLast_iter(head, 5));


    return 0;
}