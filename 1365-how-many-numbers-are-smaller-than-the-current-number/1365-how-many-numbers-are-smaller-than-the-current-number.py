class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortNums = sorted(nums)
        order = []
        for num in nums:
            for i in range(len(sortNums)):
                if sortNums[i] == num:
                    order.append(i)
                    break
        return order