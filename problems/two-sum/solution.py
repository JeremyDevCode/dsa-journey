from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in result:
                return [index, result[diff]]
            result[num] = index