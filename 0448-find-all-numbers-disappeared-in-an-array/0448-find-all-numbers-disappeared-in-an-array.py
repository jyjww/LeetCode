class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setNums = set(nums)
        missing = []
        for num in range (1, len(nums)+1):
            if num not in setNums:
                missing.append(num)

        return missing
