"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

    Input: num = 38
    Output: 2
    Explanation: The process is
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2
    Since 2 has only one digit, return it.
    Input: num = 38
    Output: 2
    Explanation: The process is
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2
    Since 2 has only one digit, return it.
"""


class Solution:
    def sum_of_digits(self, num: int) -> int:
        val = 0
        for n in str(num):
            val += int(n)
        return val


    def add_digits(self, num: int) -> int:
        if num > 0:
            res = self.sum_of_digits(num)
            while res > 9:
                res = self.sum_of_digits(res)
            return res
        if num == 0:
            return 0


test = Solution()
print(test.add_digits(38))


