class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counted = 0
        for i in details:

            if int(i[11] + i [12]) > 60:
                counted += 1

        return counted