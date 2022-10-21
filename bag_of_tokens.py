class Solution:
    def bagOfTokensScore(self, tokens, power: int) -> int:
        score = 0
        tokens.sort()
        while tokens:
            if tokens[0] <= power:
                power -= tokens.pop(0)
                score += 1
            elif tokens[0] > power and score > 0 and len(tokens) > 1:
                power += tokens.pop(-1)
                score -= 1
            else:
                break
        return score


sol = Solution()
print(sol.bagOfTokensScore([71, 55, 82], 54))
