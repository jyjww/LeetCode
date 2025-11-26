class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices[:] # 리스트 얕은 복사
        stack = []

        # 리스트의 인덱스와 값을 같이 불러오는 함수 enumerate
        for i, price in enumerate(prices):
            # 현재 price가 스택 위에 있는 값보다 작거나 같으면
            while stack and prices[stack[-1]] >=price:
                idx = stack.pop()
                res[idx] = prices[idx] - price
            stack.append(i)

        return res