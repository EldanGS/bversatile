#include <bits/stdc++.h>
#ifndef consturtor_h
#define consturtor_h

struct TreeNode {
	int value;
	TreeNode *left;
	TreeNode *right;
	TreeNode *parent; // Needed for problem 4.6

	TreeNode(int x) :
		value(x),
		left(NULL),
		right(NULL),
		parent(NULL)
	{}

	// Useful for problem 4.6
	void addLeftChild(int x) {
		TreeNode *node = new TreeNode(x);
		left = node;
		node -> parent = this;
	}

	// Useful for problem 4.6
	void addRightChild(int x) {
		TreeNode *node = new TreeNode(x);
		right = node;
		node -> parent = this;
	}

	// print Tree Pre-order traverse
	void printPreorder(TreeNode *root) {
		if (!root) {
			return;
		}
		std::cout << root -> value;
		printPreorder(root -> left);
		printPreorder(root -> right);
	}

	// print Tree In-order traverse
	void printInorder(TreeNode *root) {
		if (!root) {
			return;
		}
		printInorder(root -> left);
		std::cout << root -> value;
		printInorder(root -> right);
	}

	// print Tree Post-order traverse
	void printPostorder(TreeNode *root) {
		if (!root) {
			return;
		}
		printPostorder(root -> left);
		printPostorder(root -> right);
		std::cout << root -> value;
	}
};

struct TreeNode* newnode(int value) {
	struct TreeNode* TreeNode = (struct TreeNode*) malloc(sizeof(struct TreeNode));
	TreeNode->value = value;
	TreeNode->left = NULL;
	TreeNode->right = NULL;

	return (TreeNode);
}

#endif