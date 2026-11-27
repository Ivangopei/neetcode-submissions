class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            result = target - n
            if result in prev:
                return [nums.index(result), i]
            else:
                prev[n] = i
