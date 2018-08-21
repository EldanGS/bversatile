#include "listConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

/*
1st solution, naive hashtable algortihm.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
*/
ListNode *getIntersectionNode_naive(ListNode *headA, ListNode *headB) {
    unordered_map<ListNode*, bool> data;
    while (headA) {
        data[headA] = true;
        headA = headA -> next;
    }
    
    while (headB) {
        if (data[headB]) {
            return headB;
        }
        headB = headB -> next;
    }
    
    return NULL;
}

/*
2nd solution, optimal algortihm.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
*/
ListNode *getIntersectionNode_naive(ListNode *headA, ListNode *headB) {
    if (!headA or !headB) {
        return NULL;
    }
    
    ListNode * a = headA;
    ListNode * b = headB;
    while (a != b) {
        a = a ? a -> next : headB;
        b = b ? b -> next : headA;
    }

    return a;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    ListNode * head = NULL;
    for (int i = 3; i >= 1; i--) {
        insert(head, random_range(1, 10));
    }

    printList(head);


    return 0;
}