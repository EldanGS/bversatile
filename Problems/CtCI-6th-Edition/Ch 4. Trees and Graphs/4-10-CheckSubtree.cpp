#include "TreeNodeConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

// Solutions               Runtime                   Preference
// ------------------------------------------------------------------
// 1) Preorder Traversal   See analysis at bottom    Worth mentioning
// 2) Recursive search     See analysis at bottom    Favorite

/* Solution 1
* - Book says if T1's preorder traversal is substring of T2's preorder traversal, and same 
*   is true for inorder traversals, then T2 is substring of T1
* - During implementation, we can  insert dummy "0" for nulls. This is necessary 
*   to distinguish the 2 trees in book with duplicate values.
*/

/**************/
/* Solution 2 */
/**************/

bool matchTree(TreeNode *t1, TreeNode *t2) {
    if (t1 == NULL and t2 == NULL) {
        return true; // nothing left in the subtree
    } else if (t1 == NULL or t2 == NULL) {
        return false; // exactly tree is empty, therefore tree don't match
    }

    if (t1 -> value != t2 -> value) {
        return false; // value doesn't match
    }

    return matchTree(t1 -> left, t2 -> left)
        and matchTree(t1 -> right, t2 -> right);
}

bool subTree(TreeNode *t1, TreeNode *t2) {
    if (!t1) {
        return false;
    } 
    if (matchTree(t1, t2)) {
        return true;
    }

    return subTree(t1 -> left, t2) or subTree(t1 -> right, t2);
}

bool containsTree(TreeNode *t1, TreeNode *t2) {
    if (!t2) { // The empty tree is always a subtree
        return true;
    }
    return subTree(t1, t2);
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    /* Constructed 1st binary tree is
                5
               / \
              2   9
             /\    \
            1 4     11
                   /
                  10 

        Constructed 2nd binary subtree is   
                9
                 \
                  11
                 /
                10 
    */


    TreeNode *t1 = new TreeNode(5);
    t1 -> left = newnode(2);
    t1 -> right = newnode(9);

    t1 -> left -> left = newnode(1);
    t1 -> left -> right = newnode(4);
    t1 -> right -> right = newnode(11);

    t1 -> right -> right -> left = newnode(10);

    TreeNode *t2 = new TreeNode(9);
    t2 -> right = newnode(11);
    t2 -> right -> left = newnode(10);


    if (subTree(t1, t2)) {
        cout << "t2 Subtree is t1\n";
    } else {
        cout << "t2 not Subtree is t1\n";
    }


    return 0;
}