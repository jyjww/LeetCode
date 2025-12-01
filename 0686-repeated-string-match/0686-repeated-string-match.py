class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1

        # B 보다 길어지거나 같아질때까지 a를 늘린다. 
        while len(repeated) < len(b):
            repeated += a
            count += 1
        
        # b 가 a가 반복된 문자열에 있는 경우
        if b in repeated:
            return count
        
        # b의 시작 일부가 뒤쪽 a, 앞쪽 a에 나누어져 있는 경우.
        if b in (repeated + a):
            return count + 1
        
        # a를 b의 길이만큼 반복했음에도 반복되지 않으면, 패턴 없음
        return -1
        