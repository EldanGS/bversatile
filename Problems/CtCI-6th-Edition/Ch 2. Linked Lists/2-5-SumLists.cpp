#include "listConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

/*
1st solution, naive algortihm
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
*/
ListNode * sumLists_naive(ListNode * a, ListNode * b) {
    int valueA = 0;
    while (a) {
        valueA += a -> val;
        a = a -> next;
        if (a) {
            valueA *= 10;
        }
    }

    int valueB = 0;
    while (b) {
        valueB += b -> val;
        b = b -> next;
        if (b) {
            valueB *= 10;
        }
    }

    string convert = to_string(valueA + valueB);
    ListNode * sum = NULL;

    for (int i = (int)convert.size() - 1; i >= 0; i--) {
        insert(sum, convert[i] - '0');
    }

    return sum;
}

/*
2nd solution, more concise;
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
*/
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode * head = new ListNode(0);
    ListNode * prev = head;
    int sum = 0;
    while (l1 or l2) {
        if (l1) {
            sum += l1 -> val;
            l1 = l1 -> next;
        }
        if (l2) {
            sum += l2 -> val;
            l2 = l2 -> next;
        }
        prev -> next = new ListNode(sum % 10);
        prev = prev -> next;
        sum /= 10;
    }
    
    if (sum) {
        prev -> next = new ListNode(1);
    }
    
    return head -> next;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    ListNode * a = NULL;
    ListNode * b = NULL;
    for (int i = 3; i >= 1; i--) {
        insert(a, random_range(1, 9));
        insert(b, random_range(1, 9));
    }

    printList(a);
    cout << "+\n";
    printList(b);

    printList(sumLists(a, b));


    return 0;
}
