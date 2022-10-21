class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_list = [letter for letter in magazine]
        for i in ransomNote:
            if i not in magazine_list:
                return False
            magazine_list.remove(i)
        return True


sol = Solution()
print(sol.canConstruct('aa', 'aab'))
