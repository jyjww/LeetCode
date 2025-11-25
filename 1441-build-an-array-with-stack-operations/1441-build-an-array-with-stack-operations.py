class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        t = 0
        for i in range (1, n+1):
            if t == len(target):
                break
            stack.append("Push")
            if i == target[t]:
                t += 1
                continue
            else:
                stack.append("Pop")
        return stack