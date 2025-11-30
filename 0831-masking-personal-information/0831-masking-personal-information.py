class Solution:
    def maskPII(self, s: str) -> str:
        
        # 이메일인 경우 @가 들어감

        a = s.rfind("@")
        
        if a > -1:
            arr = s.lower().split("@")
            email = arr[0]
            pt1 = email[0] + "*" * 5 + email[-1]
            pt2 = arr[1]
            return pt1 + "@" + pt2
        # 핸드폰인 경우 -가 들어감

        else:
            ast = "*" * 3
            digits = "".join(ch for ch in s if ch.isdigit())
            n = len(digits)
            end = digits[-4:]

            if n == 10 :
                return ast + "-" + ast + "-" + end
            else:
                code = "+" + "*" * (n - 10)
                return code + "-" + ast + "-" + ast + "-" + end