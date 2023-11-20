"""
Given an array of strings words, return the words that can be typed using letters of the alphabet
on only one row of American keyboard like the image below.
"""

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        q = frozenset(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        a = frozenset(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        z = frozenset(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        res_list = []
        for word in words:
            word_set = set(word.lower())
            if len(word_set) == len(word_set & a) \
                    or len(word_set) == len(word_set & q) \
                    or len(word_set) == len(word_set & z):
                        res_list.append(word)
        return res_list


sol = Solution()
print(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]))










