#include <bits/stdc++.h>
#ifndef consturtor_h
#define consturtor_h

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) :
        val(x),
        next(NULL)
    {}
};

/**
 * [insert - insert a node at the head of list]
 * @param head [head of the list]
 * @param data [new node's data]
 */
void insert(ListNode* &head, int val) {
    ListNode * newListNode = new ListNode(val);
    newListNode -> next = head;
    head = newListNode;
}

/**
 * [printList Helper routine to print list]
 * @param head [head of the list]
 */
void printList(ListNode * head) {
    while (head) {
        std::cout << head -> val << "-->";
        head = head -> next;
    }
    std::cout << "nullptr\n";
}

//generate a random int between min and max
/**
 * [random_range helper routine to generate a random number between min and max (including)]
 * @param  min [min of range]
 * @param  max [max of range]
 * @return     [A random number between min and max]
 */
static inline int random_range(const int min, const int max) {
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<int> distribution(min, max);
    return distribution(mt);
}

#endif