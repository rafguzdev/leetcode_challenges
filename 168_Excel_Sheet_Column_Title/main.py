# SOLUTION 1
class Solution:
    val = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K',
           12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
           22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

    def convertToTitle(self, columnNumber: int) -> str:
        out = ''
        while columnNumber != 0:
            columnNumber -= 1
            temp = columnNumber % 26
            out += self.val[temp+1]
            columnNumber = columnNumber // 26
        return out[::-1]


my = Solution()
print(my.convertToTitle(27))
