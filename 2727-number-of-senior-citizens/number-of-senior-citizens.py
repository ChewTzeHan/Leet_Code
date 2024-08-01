class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counted = 0
        for i in details:
            age = int(i[11] + i [12])
            print(age)
            if age > 60:
                counted += 1

        return counted