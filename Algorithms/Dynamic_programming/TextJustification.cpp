/**
 * Video link - https://youtu.be/RORuwHiblPc
 * 
 * Given a sequence of words, and a limit on the number of characters that can be put 
 * in one line (line width). Put line breaks in the given sequence such that the 
 * lines are printed neatly
 * 
 * Solution:
 * Badness - We define badness has square of empty spaces in every line. So 2 empty space
 * on one line gets penalized as 4 (2^2) while 1 each empty space on 2 lines gets
 * penalized as 2(1 + 1). So we prefer 1 empty space on different lines over 2 empty space on
 * one line.
 * 
 * For every range i,j(words from i to j) find the cost of putting them on one line. If words 
 * from i to j cannot fit in one line cost will be infinite. Cost is calculated as square of
 * empty space left in line after fitting words from i to j.
 * 
 * Then apply this formula to get places where words need to be going on new line.
 * minCost[i] = minCost[j] + cost[i][j-1]
 * Above formula will try every value of j from i to len and see which one gives minimum 
 * cost to split words from i to len.
 * 
 * Space complexity is O(n^2)
 * Time complexity is O(n^2)
 * 
 * References:
 * http://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/
 */
 
 
 #include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define frp freopen("input.txt", "r", stdin); \
            freopen("output.txt", "w", stdout); 

int main() { // frp
    vector <string> words{"Eldan", "really", "want", "road", "to", "target"};
    int limit = 12;

    int n = (int)words.size();
    vector <vector <int> > cost(n, vector <int> (n));

    for (int i = 0; i < n; i++) {
        cost[i][i] = limit - (int)words[i].size();

        for (int j = i + 1; j < n; j++) {
            cost[i][j] = cost[i][j - 1] - (int)words[j].size() - 1;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (cost[i][j] < 0) {
                cost[i][j] = INT_MAX;
            } else {
                cost[i][j] *= cost[i][j];
            }
        }
    }

    vector <int> minCost(n, 0);
    vector <int> result(n, 0);

    for (int i = n - 1; i >= 0; i--) {
        minCost[i] = cost[i][n - 1];
        result[i] = n;

        for (int j = n - 1; j > i; j--) {
            if (cost[i][j - 1] == INT_MAX) {
                continue;
            }

            if (minCost[i] > minCost[j] + cost[i][j - 1]) {
                minCost[i] = minCost[j] + cost[i][j - 1];
                result[i] = j;
            }
        }
    }


    cout << "Minimum cost is " << minCost[0] << "\n";

    int i = 0, j = 0;
    string text = "";

    do {
        j = result[i];
        for (int index = i; index < j; index++) {
            text += (words[index] + " ");
        }
        text += ("\n");
        i = j;
    } while(j < n);

    for (int i = 0; i < (int)text.size(); i++) {
        cout << text[i];
    }


    return 0;
}
