#include "listConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

/*
1st solution, naive algortihm
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
*/
bool hasCycle(ListNode * head) {
    if (!head) {
        return false;
    }

    unordered_map<ListNode*, bool> data;
    while (head) {
        if (data[head]) {
            return true;
        }

        data[head] = true;
        head = head -> next;
    }

    return false;
}

/*
2nd solution, optimal algortihm
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
*/
bool hasCycle(ListNode * head) {
    if (!head) {
        return false;
    }

    ListNode * walker = head;
    ListNode * runner = head;

    while (runner -> next and runner -> next -> next) {
        walker = walker -> next;
        runner = runner -> next -> next;

        if (walker == runner) {
            return true;
        }
    }

    return false;
}   

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    ListNode * head = NULL;
    for (int i = 10; i >= 1; i--) {
        insert(head, random_range(1, 10));
    }

    printList(head);


    return 0;
}
