class Solution:
    def romanToInt(self, s: str) -> int:
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        numerals = [1000, 900, 500, 400, 100, 90, 50, 40 ,10 ,9 ,5, 4, 1]

        num = 0
        count = 0
        while s or count == 20:
            count += 1
            print(s, num)
            single = s[0]
            if len(s) > 1:
                double = s[0] + s[1]
            else:
                double = ''

            for i in range(len(romans)):
                if romans[i] == double:
                    num += numerals[i]
                    s = s.replace(romans[i], '', 1)
                    break

                elif romans[i] == single:
                    num += numerals[i]
                    s = s.replace(romans[i], '', 1)
                    break

        return num
