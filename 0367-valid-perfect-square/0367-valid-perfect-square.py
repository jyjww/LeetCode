class Solution(object):
    def isPerfectSquare(self, num):
        
        result = 0
        if num == 1 :
            return bool(1)
        left = 1
        right = num

        while left <= right :
            mid = (left + right) // 2

            if mid ** 2 == num:
                return bool(1)
            if mid ** 2 > num :
                right = mid - 1
            else : 
                left = mid + 1
        return bool(0)
