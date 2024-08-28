""" 
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
#Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.  
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == ""):
            return 0
        results = []
        tmp = []
        for x in s:
            if(tmp.count(x) > 0):
                results.append(len(tmp))
                tmp = []
        if(results == []):
            return 1
        results.sort()
        results.reverse()
        return results.pop()
    
    
solution = Solution()
print(solution.lengthOfLongestSubstring("")) #0
print(solution.lengthOfLongestSubstring("1231")) #1
print(solution.lengthOfLongestSubstring("     ")) #1