class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            new = [0] * (len(res) + 1)
            for j in range(len(res)):
                new[j] += res[j]
                new[j+1] += res[j]
            res = new
        return res