class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        output = 0

        for i in range(len(s)):
            if i < len(s)-1:
                if dict.get(s[i]) >= dict.get(s[i+1]):
                    output += dict.get(s[i])
                else:
                    #output = output+dict.get(s[i+1])
                    output = output-dict.get(s[i])
                    i +=1
            else:
                output = output + dict.get(s[i])
        return output