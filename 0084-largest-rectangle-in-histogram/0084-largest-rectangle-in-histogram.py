class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = [0] * len(heights)
        stack = []

        for i, height in enumerate(heights):
            # 나보다 작은 막대를 만난 순간 pop 하고 넓이 확정
            while stack and heights[stack[-1]] > height:
                idx = stack.pop()
                right = i
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                width = right - left - 1
                res[idx] = heights[idx] * width
            stack.append(i)

        # 끝까지 나보다 큰 막대를 못만난 경우 처리
        right = len(heights)
        while stack:
            idx = stack.pop()
            height = heights[idx]
            left = stack[-1] if stack else -1
            width = right - left - 1
            res[idx] = height * width
                
        return max(res)