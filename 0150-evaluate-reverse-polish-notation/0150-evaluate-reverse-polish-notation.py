class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        nums = []
        for token in tokens:
            if token in operators:
                a = nums.pop()
                b = nums.pop()
                if token == "+":
                    nums.append(b+a)
                elif token == "-":
                    nums.append(b-a)
                elif token == "*":
                    nums.append(b*a)
                else:
                    nums.append(int(b/a))
            else: 
                nums.append(int(token))
        return nums[0]