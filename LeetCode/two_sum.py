"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2, 7, 11, 15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


def two_sum(numbers: list, target: int) -> list:
    for ind, val_a in enumerate(numbers):
            val_b = target - val_a
            if val_b in numbers and ind != numbers.index(val_b):
                return [ind, numbers.index(val_b)]


numbers = [2, 7, 11, 15]
target = 9
answer = two_sum(numbers, target)
print(answer)