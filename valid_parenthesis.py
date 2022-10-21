class Solution:
    def isValid(self, s: str) -> bool:
        bra_count, sqbra_count, curlybra_count = 0, 0, 0
        last = []
        for i in s:
            try:
                if i == "(":
                    bra_count += 1
                    last += ["bra"]
                elif i == ")" and last[-1] == "bra":
                    bra_count -= 1
                    last.pop()
                elif i == "[":
                    sqbra_count += 1
                    last += ["sq"]
                elif i == "]" and last[-1] == "sq":
                    sqbra_count -= 1
                    last.pop()
                elif i == "{":
                    curlybra_count += 1
                    last += ["curl"]
                elif i == "}" and last[-1] == "curl":
                    curlybra_count -= 1
                    last.pop()
                else:
                    return False

                if bra_count < 0 or curlybra_count < 0 or sqbra_count < 0:
                    return False

            except:
                return False

        if bra_count == sqbra_count == curlybra_count == 0:
            return True

        return False


sol = Solution()
print(sol.isValid("}"))

# ++++++++++++++++++OR+++++++++++++++++++


def isValid(s: str) -> bool:

    stack = []

    if len(s) <= 1:
        return False
    else:
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack += i
            else:
                if len(stack) == 0:
                    return False
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

    if stack:
        return False
    return True


print(isValid("(])"))
