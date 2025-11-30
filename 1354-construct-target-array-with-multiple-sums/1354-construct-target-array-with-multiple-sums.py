class Solution:
    def isPossible(self, target: List[int]) -> bool:
        arr = []
        for t in target:
            heapq.heappush(arr, -t)

        total = sum(target)
        while True:
            x = -heapq.heappop(arr)
            rest = total - x

            if x == 1 or rest == 1 :
                return True
            
            if rest <= 0 or x < rest:
                return False

            newVal = x % rest
            if newVal == 0:
                return False
            
            heapq.heappush(arr, -newVal)
            total = rest + newVal
            