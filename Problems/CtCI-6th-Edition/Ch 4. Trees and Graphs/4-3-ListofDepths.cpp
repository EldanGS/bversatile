#include "TreeNodeConstructor.h"
#include "ListConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

void addChild(TreeNode * node, vector<TreeNode *> &list);

vector<vector<TreeNode* > > ListOfDepths(TreeNode *root) {
    vector<vector<TreeNode* > > result;
    if (!root) {
    	return result;
    }

    vector<TreeNode *> current{root};
    while (!current.empty()) {
    	result.push_back(current);

    	vector<TreeNode *> prev = current;
    	current = vector<TreeNode *>();
    	for (auto it : prev) {
    		addChild(it, current);
    	}
    }

    return result;
}

void addChild(TreeNode *node, vector<TreeNode *> &list) {
	if (node -> left) {
		list.push_back(node -> left);
	} 
	if (node -> right) {
		list.push_back(node -> right);
	}
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
	/* Constructed binary tree is
	            10
	          /   \
	        8      2
	      /
	    3
  	*/
    TreeNode * root = new TreeNode(10);
    root -> left = newnode(8);
    root -> right = newnode(2);
    root -> left -> left = newnode(3);

    // Print all possible connection
    auto result = ListOfDepths(root);
    int level = 0;
    for (vector<TreeNode *> list : result) {
    	cout << "level = " << ++level << "\n";
    	for (auto it : list) {
    		// if there is no child, then -1 otherwise print child
    		cout << "root -> " << it -> value << "\n";
    		cout << "left child -> " << (it -> left ? it -> left -> value : -1) << "\n";
    		cout << "right child -> " << (it -> right ? it -> right -> value : -1) << "\n";
    	}
    	cout << "\n";
    }

    /*
    level = 1
	root -> 10
	left child -> 8
	right child -> 2

	level = 2
	root -> 8
	left child -> 3
	right child -> -1
	root -> 2
	left child -> -1
	right child -> -1

	level = 3
	root -> 3
	left child -> -1
	right child -> -1
	*/


    return 0;
}
