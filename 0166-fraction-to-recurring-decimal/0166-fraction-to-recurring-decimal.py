class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0 :
            return "0"
        
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0) :
            result = "-"
        else :
            result = ""

        n = abs(numerator)
        d = abs(denominator)

        result += str(n//d)
        rem = n % d

        if rem == 0 :
            return result

        result += "."
        dict = {}

        while rem > 0 :
            if rem in dict :
                result = result[:dict[rem]] + "(" + result[dict[rem]:] + ")"
                break
            dict[rem] = len(result)
            rem = rem * 10

            result += str(rem // d)
            rem = rem % d
        return result
        
        

        