class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [''] * numRows
        if numRows == 1:
            return s

        if numRows == 2:
            count = 0
            
            for i in s:
                zigzag[count] += i
                count += 1
                if count > 1:
                    count = 0

            ans = ''
            for i in zigzag:
                ans += i
            return ans


        vertical = 0
        diagonal = numRows - 2
        for i in s:
            if vertical < numRows:
                zigzag[vertical] += i
                vertical += 1

            else:
                zigzag[diagonal] += i
                diagonal -= 1

            if diagonal == 0:
                vertical = 0
                diagonal = numRows - 2
            #print(zigzag)

        ans = ''
        for i in zigzag:
            ans += i

        return ans
 #PAHN APLSIIG YIR