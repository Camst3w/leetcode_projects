class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1000: "M", 900: "CM",
            500: "D",  400: "CD",
            100: "C",  90: "XC",
            50: "L",   40: "XL",
            10: "X",   9: "IX",
            5: "V",    4: "IV",
            1: "I",
        }
        roman = ""
        num_set = symbols.keys()
        while num > 0:
            for i in num_set:
                if num - i >= 0:
                    num -= i
                    roman += symbols.get(i)
                    break
                else:
                    num_set.remove(i)
        return roman


sol = Solution()
print(sol.intToRoman(1994))
