class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 첫 문자가 대문자면, 모든 문자가 대문자거나, 뒤에 나오는 모든 문자가 소문자여야 한다. 
        # 첫 문자가 소문자면, 모든 문자가 소문자여야 한다. 

        if word.isupper() == True:
            return True
        elif word.islower() == True:
            return True
        elif word[0].isupper() == True and word[1:].islower() == True:
            return True
        else:
            return False
