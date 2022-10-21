class Solution:
    def validUtf8(self, data) -> bool:
        test = True
        bin_data = [decimalToBinary(i) for i in data]
        i = 0
        while i < len(bin_data):
            try:
                if bin_data[i][0] == "0":
                    i += 1
                elif (bin_data[i][:3] == "110") and (bin_data[i+1][:2] == "10"):
                    i += 2
                elif (bin_data[i][:4] == "1110") and (bin_data[i+1][:2] == bin_data[i+2][:2] == "10"):
                    i += 3
                elif (bin_data[i][:5] == "11110") and (bin_data[i+1][:2] == bin_data[i+2][:2] == bin_data[i+3][:2] == "10"):
                    i += 4
                else:
                    test = False
                    i = len(bin_data) + 1
            except:
                test = False
                i = len(bin_data) + 1
        return test


def decimalToBinary(n):
    binary = "{0:b}".format(int(n))
    difference = 8 - len(binary)
    return ("0" * difference) + binary


sol = Solution()
print(sol.validUtf8([235, 140, 4]))
