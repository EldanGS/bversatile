#include "TreeNodeConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

/*
1st solution.
Complexity analysis:
Time: O(NlogN) - always
Memory: O(NlogN) - in worst case
*/
int countPathsWithSumFromNode(TreeNode *node, int target, int currentSum) {
    if (node == NULL) {
        return 0;
    }

    currentSum += node -> value;
    
    int totalPaths = 0;
    if (currentSum == target) {
        totalPaths++;
    }
    
    totalPaths += countPathsWithSumFromNode(node -> left, target, currentSum);
    totalPaths += countPathsWithSumFromNode(node -> right, target, currentSum);

    return totalPaths;
}

int PathsWithSum(TreeNode *root, int target) {
    if (root == NULL) {
        return 0;
    }

    int pathsFromRoot = countPathsWithSumFromNode(root, target, 0);
    int pathsFromLeft = PathsWithSum(root -> left, target);
    int pathsFromRight = PathsWithSum(root -> right, target);

    return pathsFromRoot + pathsFromLeft + pathsFromRight;
}

/*
2nd solution.
Complexity analysis:
Time: O(N) - always
Memory: O(N) - in worst case
*/
int countPathsWithSum(TreeNode *node, int target, int runningSum, unordered_map<int, int> pathCount);
void incrementHashTable(unordered_map<int, int> &pathCount, int key, int delta);

int countPathsWithSum(TreeNode *root, int target) {
    unordered_map<int, int> hash;
    return countPathsWithSum(root, target, 0, hash);
}

int countPathsWithSum(TreeNode *node, int target, int runningSum, unordered_map<int, int> pathCount) {
    if (node == NULL) {
        return 0;
    }

    runningSum += node -> value;
    int sum = runningSum - target;
    int totalPaths = pathCount[sum];

    if (runningSum == target) {
        totalPaths++;
    }

    // increment path, recurse, then decrement pathCount.
    incrementHashTable(pathCount, runningSum, 1); // increment pathCount
    totalPaths += countPathsWithSum(node -> left, target, runningSum, pathCount);
    totalPaths += countPathsWithSum(node -> right, target, runningSum, pathCount);
    incrementHashTable(pathCount, runningSum, -1); // decrement pathCount

    return totalPaths;
}

void incrementHashTable(unordered_map<int, int> &pathCount, int key, int delta) {
    int newCount = pathCount[key] + delta;
    if (newCount == 0) {
        pathCount.erase(key);
    } else {
        pathCount[key] = newCount;
    }
}


int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    /* Constructed binary tree is
                 6
               /  \
              3    5
             /\   / \
            1 2  4  7
             /   
            8            
    */

    TreeNode *tree = new TreeNode(6);
    tree -> left = newnode(3);
    tree -> right = newnode(5);

    tree -> left -> left = newnode(1);
    tree -> left -> right = newnode(2);
    tree -> right -> left = newnode(4);
    tree -> right -> right = newnode(7);

    tree -> left -> right -> left = newnode(8);
    
    int target = 11;

    cout << countPathsWithSum(tree, target) << "\n"; 


    return 0;
}