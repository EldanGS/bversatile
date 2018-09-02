#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

class BST {
    struct TreeNode {
        int value;
        int size;
        TreeNode *left;
        TreeNode *right;
    };

    TreeNode *root;

    TreeNode *clear(TreeNode *node) {
        if (!node) {
            return NULL;
        }
        {
            clear(node -> left);
            clear(node -> right);
            delete node;   
        }
        return NULL;
    }

    TreeNode *find(TreeNode *node, int x) {
        if (node == NULL or node -> value == x) {
            return node;
        }
        if (node -> value < x) {
            return find(node -> right, x);
        }

        return find(node -> left, x);
    }

    TreeNode *insert(TreeNode *node, int x) {
        if (node == NULL) {
            node = new TreeNode;
            node -> size++;
            node -> value = x;
            node -> left = node -> right = NULL;
        } else if (node -> value > x) {
            node -> left = insert(node -> left, x);
        } else if (node -> value < x) {
            node -> right = insert(node -> right, x);
        } 
        return node;
    }

    TreeNode *findMin(TreeNode *node) {
        if (node == NULL) {
            return node;
        } else if (node -> left == NULL) {
            return node;
        }
        return findMin(node -> left);
    }

    TreeNode *findMax(TreeNode *node) {
        if (node == NULL) {
            return node;
        } else if (node -> right == NULL) {
            return node;
        }
        return findMax(node -> right);
    }

    TreeNode *remove(TreeNode *node, int x) {
        TreeNode *temp;
        if (node == NULL) {
            return NULL;
        }
        if (node -> value > x) {
            node -> left = remove(node -> left, x);
        } else if (node -> value < x) {
            node -> right = remove(node -> right, x);
        } else if (node -> left and node -> right) {
            temp = findMin(node -> right);
            node -> value = temp -> value;
            node -> right = remove(node -> right, node -> value);
        } else {
            temp = node;
            if (node -> left == NULL) {
                node = node -> right;
            } else if (node -> right == NULL) {
                node = node -> left;
            }

            delete temp;
        }

        return node;
    }

    void getRandom(TreeNode *node) {
        if (node == NULL) {
            cout << "NOT FOUND\n";
            return;
        }
        int x = (int)(random() * node -> size);
        
        cout << find(node, x) << "\n";
    }

    void inorder(TreeNode *node) {
        if (!node) {
            return;
        }
        inorder(node -> left);
        cout << node -> value << " ";
        inorder(node -> right);
    }
public:
    BST() {
        root = NULL;
    }

    ~BST() {
        clear(root);
    }

    void insert(int x) {
        root = insert(root, x);
    }

    void remove(int x) {
        root = remove(root, x);
    }

    void find(int x) {
        root = find(root, x);
    }

    void getRandom() {
        cout << "Get random element\n"; 
        getRandom(root);
    }

    void print() {
        inorder(root);
        cout << "\n";
    }
};


int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    BST tree;
    tree.insert(10);
    tree.insert(6);
    tree.insert(15);
    tree.insert(8);
    tree.insert(4);
    tree.insert(13);
    tree.insert(18);
    tree.print();
    tree.getRandom();
    tree.remove(8);
    tree.remove(13);
    tree.print();

    return 0;
}