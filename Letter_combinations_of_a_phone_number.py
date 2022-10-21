class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        COMBINATIONS = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        counts, combines = len(digits), []

        if counts == 0:
            return combines

        if counts == 1:
            return COMBINATIONS[digits]
        
        if counts == 2:
            for i in COMBINATIONS[digits[0]]:
                for j in COMBINATIONS[digits[1]]:
                    combines.append(i + j)
            return combines

        if counts == 3:
            for i in COMBINATIONS[digits[0]]:
                for j in COMBINATIONS[digits[1]]:
                    for k in COMBINATIONS[digits[2]]:
                        combines.append(i + j + k)
            return combines

        if counts == 4:
            for i in COMBINATIONS[digits[0]]:
                for j in COMBINATIONS[digits[1]]:
                    for k in COMBINATIONS[digits[2]]:
                        for l in COMBINATIONS[digits[3]]:
                            combines.append(i + j + k + l)
            return combines

    def letterCombinations(self, digits):
        pass  
        
        

sol = Solution()
print(sol.letterCombinations("23"))