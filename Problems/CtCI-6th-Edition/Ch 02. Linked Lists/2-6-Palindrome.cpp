#include "listConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

/*
1st solution, naive algortihm.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
*/
bool isPalindrome_naive(ListNode * head) {
    if (!head or (head and !head -> next)) {
        return true;
    }
    string s = "";
    while (head) {
        s += ((head -> val) + '0');
        head = head -> next;
    }

    for (int i = 0; i < (int)s.size() / 2; i++) {
        if (s[i] != s[(int)s.size() - i - 1]) {
            return false;
        }
    }

    return true;
}

/*
2nd solution, concise algorithm.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
*/
bool isPalindrome_stack(ListNode * head) {
    if (!head or (head and !head -> next)) {
        return true;
    }
    stack<int> st;
    ListNode * ptr = head;
    while (ptr) {
        st.push(ptr -> val);
        ptr = ptr -> next;
    }

    while (head) {
        if (head -> val != st.top()) {
            return false;
        }
        head = head -> next;
        st.pop();
    }

    return true;
}

/*
3rd solution, optimal algorithm.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
*/
ListNode * reverseList(ListNode * head) {
    ListNode * prev = NULL;
    while (head) {
        ListNode * step = head -> next;
        head -> next = prev;
        prev = head;
        head = step;
    }
    
    return prev;
}

bool isPalindrome(ListNode * head) {
    if (!head or (head and !head -> next)) {
        return true;
    }
    ListNode * walker = head;
    ListNode * runner = head;

    while (runner -> next and runner -> next -> next) {
        walker = walker -> next;
        runner = runner -> next -> next;
    }

    walker -> next = reverseList(walker -> next);
    walker = walker -> next;

    while (walker) {
        if (walker -> val != head -> val) {
            return false;
        }
        walker = walker -> next;
        head = head -> next;
    }

    return true;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    ListNode * head = NULL;
    for (int i = 3; i >= 1; i--) {
        insert(head, random_range(1, 2));
    }

    printList(head);
    if (isPalindrome(head)) {
        cout << "Palindrome\n";
    } else {
        cout << "Not palindrome\n";
    }


    return 0;
}