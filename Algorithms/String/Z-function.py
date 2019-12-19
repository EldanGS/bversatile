"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.

"""


"""
Algorithm

Our loop invariants will be that center, right is our knowledge of the 
palindrome with the largest right-most boundary with center < i, centered at 
center with right-boundary right. Also, i > center, and we've already 
computed all Z[j]'s for j < i. 

When i < right, we reflect i about center to be at some coordinate j = 2 * 
center - i. Then, limited to the interval with radius right - i and center i, 
the situation for Z[i] is the same as for Z[j]. 

For example, if at some time center = 7, right = 13, i = 10, then for a 
string like A = '@#A#B#A#A#B#A#＄', the center is at the '#' between the two 
middle 'A''s, the right boundary is at the last '#', i is at the last 'B', 
and j is at the first 'B'. 

Notice that limited to the interval [center - (right - center), right] (the 
interval with center center and right-boundary right), the situation for i 
and j is a reflection of something we have already computed. Since we already 
know Z[j] = 3, we can quickly find Z[i] = min(right - i, Z[j]) = 3. 

Now, why is this algorithm linear? The while loop only checks the condition 
more than once when Z[i] = right - i. In that case, for each time Z[i] += 1, 
it increments right, and right can only be incremented up to 2*N+2 times. 

Finally, we sum up (v+1) / 2 for each v in Z. Say the longest palindrome with 
some given center C has radius R. Then, the substring with center C and 
radius R-1, R-2, R-3, ..., 0 are also palindromes. Example: abcdedcba is a 
palindrome with center e, radius 4: but e, ded, cdedc, bcdedcb, and abcdedcba 
are all palindromes. 

We are dividing by 2 because we were using half-lengths instead of lengths. 
For example we actually had the palindrome a#b#c#d#e#d#c#b#a, so our length 
is twice as big. 
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        s = "@#" + '#'.join(s) + '#$'
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n - 1):
            if i < r:
                z[i] = min(r - i, z[2 * l - i])
            while s[i + z[i] + 1] == s[i - z[i] - 1]:
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]

        return sum((v + 1) // 2 for v in z)

