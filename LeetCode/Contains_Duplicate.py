class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return True if len(nums) > len(set(nums)) else False


sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 4, 4]))