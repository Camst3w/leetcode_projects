class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left, right, max_diff = 0, 0, 0

        while right < len(s):
            right = left
            characters = []
            for i in s[left:]:
                if i not in characters:
                    right += 1
                    characters.append(i)
                else:
                    if right - left > max_diff:
                        max_diff = right - left
                    left += 1
                    break
            if right - left > max_diff:
                max_diff = right - left
        return max_diff


test = Solution()
print(test.lengthOfLongestSubstring("af"))
