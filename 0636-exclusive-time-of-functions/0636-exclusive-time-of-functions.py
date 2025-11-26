class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        previous = 0

        for l in logs:
            i, type, time = l.split(":")
            i, time = int(i), int(time)

            if type == "start":
                # 이미 실행중인 함수가 있는 경우 time - previous 만큼 실행
                if stack:
                    res[stack[-1]] += time - previous
                stack.append(i)
                previous = time
            else:
                res[stack[-1]] += time - previous + 1
                stack.pop()
                previous = time + 1
        return res