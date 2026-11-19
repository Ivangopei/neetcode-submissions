class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}                      # value -> index
        for i, n in enumerate(nums):
            diff = target - n           # the value we need to have seen
            if diff in saved:
                return [saved[diff], i] # earlier index first
            saved[n] = i