class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = "".join([i for i in s if i.isalnum()]).lower()
        half = len(str)//2
        forward = str[:half]
        if len(str) % 2 == 0:
            backward = str[:half-1:-1]
        else:
            backward = str[:half:-1]
        print(f"{forward} \n{backward}")
        if forward == backward:
            return True
        return False


sol = Solution()
print(sol.isPalindrome(
    "A a"))
