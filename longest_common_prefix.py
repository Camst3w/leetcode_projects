class Solution:
    def longestCommonPrefix(self, strs) -> str:
        current_longest = strs[0]
        while True:
            if current_longest == '':
                break

            check = True
            for i in range(1, len(strs)):
                if current_longest != strs[i][:len(current_longest)]:
                    current_longest = current_longest[:len(current_longest) - 1]
                    check = False
                    break
            
            if check:
                break
                
        return current_longest


sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))