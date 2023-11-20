"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))