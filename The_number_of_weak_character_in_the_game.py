class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        properties.sort(key=lambda character: character[1])
        properties.sort(key=lambda character: character[0], reverse=True)
        best_defence = properties[0][1]
        weak_characters = 0
        for index in range(len(properties)):
            if best_defence > properties[index][1]:
                weak_characters += 1
            else:
                best_defence = properties[index][1]
        return weak_characters


sol = Solution()
print(sol.numberOfWeakCharacters(
    [[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]]))
