class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            left = target - n
            if left in prev:
                return [nums.index(left), i]
            else:
                prev[n] = i