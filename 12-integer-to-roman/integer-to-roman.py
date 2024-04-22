class Solution:
    def intToRoman(self, num: int) -> str:
        digits = len(str(num))

        '''
        M = 1000
        CM = 900
        D = 500
        CD = 400
        C = 100
        XC = 90
        L = 50
        XL = 40
        X = 10
        IX = 9
        V = 5
        IV = 4
        I = 1
        '''
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        numerals = [1000, 900, 500, 400, 100, 90, 50, 40 ,10 ,9 ,5, 4, 1]

        roman = ''
        if num >= 2000:
            roman += 'M' * (floor(num/1000) - 1)
            num -= 1000 * (floor(num/1000) - 1)
            print(num)

        for i in range(len(romans)):
            print(num)
            if (num - numerals[i]) >= 0:
                roman += romans[i] * (floor(num/numerals[i]))
                num -= numerals[i] * (floor(num/numerals[i]))
            
        return roman