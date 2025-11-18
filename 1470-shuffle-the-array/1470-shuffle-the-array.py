class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        temp1 = []
        temp2 = []
        for i in range(len(nums)):
            if i < n:
                temp1.append(nums[i])
            else:
                temp2.append(nums[i])
        for i in range(n):
            result.append(temp1[i])
            result.append(temp2[i])
        return result