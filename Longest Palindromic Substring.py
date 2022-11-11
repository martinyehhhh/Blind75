"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def getLen(l,r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        start = 0
        maxLen = 0
        for i in range(n):
            currentLen = max(getLen(i,i),getLen(i,i+1))
            if currentLen > maxLen:
                maxLen = currentLen
                start =  i - (currentLen - 1) // 2
        return s[start:start+maxLen]