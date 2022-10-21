class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        number = ""
        if s[0] == "-":
            sign *= -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        if not s[0].isnumeric():
            return 0
        for i in s:
            if i.isnumeric():
                number += i
            else:
                break
        number = int(number) * sign
        high_lim, low_lim = 2**31 - 1, -2**31
        if number >= high_lim:
            return high_lim
        elif number <= low_lim:
            return low_lim
        return number


sol = Solution()
print(sol.myAtoi("     +42  just a  testt"))
