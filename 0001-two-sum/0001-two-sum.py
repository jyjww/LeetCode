class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range (len(nums)):
            x = nums[i]
            need = target - x

            if need in dict:
                return [dict[need], i]
            dict[x] = i