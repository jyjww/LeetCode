class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = []
        count = 0
        while count <= 1:
            count += 1
            for i in range (len(nums)):
                temp.append(nums[i])
        return temp