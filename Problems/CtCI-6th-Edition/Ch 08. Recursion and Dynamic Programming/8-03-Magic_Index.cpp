#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

int magicIndex(vector<int> nums, int left, int right);
int magicIndex(vector<int> nums) {
    return magicIndex(nums, 0, nums.size() - 1);
}

int magicIndex(vector<int> nums, int left, int right) {
    if (left < right) {
        return -1;
    }

    int mid = (left + right) / 2;
    if (nums[mid] == mid) {
        return mid;
    } else if (nums[mid] > mid) {
        return magicIndex(nums, left, mid - 1);
    } else {
        return magicIndex(nums, mid + 1, right);
    }
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    vector<int> v; 
    v.push_back(-10);
    v.push_back(-1);
    v.push_back(2);
    v.push_back(2);
    v.push_back(2);
    v.push_back(3);
    v.push_back(5);
    v.push_back(8);
    v.push_back(9);
    v.push_back(12);
    v.push_back(13);

    cout << magicIndex(v) << "\n";

    return 0;
}