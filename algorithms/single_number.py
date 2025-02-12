"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:
Input: nums = [2,2,1]
Output: 16

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

nums = [4, 1, 2, 1, 2]
s_nums = set(nums)
for i in s_nums:
    if nums.count(i) == 1:
        print(i)
        break

