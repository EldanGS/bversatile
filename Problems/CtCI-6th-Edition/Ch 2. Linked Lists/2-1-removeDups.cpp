#include "listConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

/*
1st solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
*/
void removeDuplicates(Node * head) {
    if (!head or (head and !head -> next)) {
        return;
    }

    unordered_set<int> node_data;
    Node * prev = head;
    Node * curr = head -> next;
    node_data.insert(head -> val);

    while (curr) {
        while (curr and node_data.find(curr -> val) != node_data.end()) {
            curr = curr -> next;
        }
        prev -> next = curr;
        prev = curr;
        if (curr) {
            node_data.insert(curr -> val); 
            curr = curr -> next;
        }
    } 
}

/*
2nd solution.
Complexity analysis:
Time: O(N^2) - always
Memory: O(1) - in worst case
*/
void removeDuplicates_naive(Node * head) {
    if (!head or (head and !head -> next)) {
        return;
    }

    Node * curr = head;

    while (curr) {
        Node * runner = curr;
        while (runner -> next) {
            if (runner -> next -> val == curr -> val) {
                runner -> next = runner -> next -> next;
            } else {
                runner = runner -> next;
            }
        }

        curr = curr -> next;
    }
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    Node * head = NULL;
    for (int i = 0; i < 10; i++) {
        insert(head, random_range(1, 10));
    }

    printList(head);
    removeDuplicates_naive(head);
    printList(head);


    return 0;
}