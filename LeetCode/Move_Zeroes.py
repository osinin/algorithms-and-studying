"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(0, nums.count(0)):
        nums.remove(0)
        nums.append(0)
    return nums


a = moveZeroes(nums=[0,1,0,3,12])
print(a)