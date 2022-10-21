class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = [i for i in dominoes]
        while True:
            test = dominoes[:]
            test_indexes = [i for i in range(
                len(dominoes)) if dominoes[i] != "."]
            for i in test_indexes:
                if i - 1 >= 0:
                    if dominoes[i] == "L" and dominoes[i-1] == ".":
                        try:
                            if dominoes[i-2] != "R":
                                test[i-1] = "L"
                        except:
                            test[i-1] = "L"
                if i + 1 < len(dominoes):
                    if dominoes[i] == "R" and dominoes[i+1] == ".":
                        try:
                            if dominoes[i+2] == "." and dominoes[i+3] == "L":
                                test[i+1] = "R"
                                test[i+2] = "L"
                            elif dominoes[i+2] != "L":
                                test[i+1] = "R"
                        except:
                            test[i+1] = "R"
            if test == dominoes:
                break
            dominoes = test[:]
        return ''.join(dominoes)


class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        while True:
            test = dominoes[:]
            test = test.replace("R.L", "xxx")
            test = test.replace("R.", "RR")
            test = test.replace(".L", "LL")
            if test == dominoes:
                break
            dominoes = test[:]
        dominoes = dominoes.replace("xxx", "R.L")
        return dominoes


sol = Solution()
print(sol.pushDominoes(".L.R...LR..L.."))
