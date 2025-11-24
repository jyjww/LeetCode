class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        dup, sumNum, S = 0, 0, 0
        for num in nums:
            if num in seen:
                dup = num
            else:
                seen.add(num)

        for num in nums:
            sumNum += num
        for i in range (1, len(nums)+1):
            S += i
        missing = S + dup - sumNum

        return [dup, missing]