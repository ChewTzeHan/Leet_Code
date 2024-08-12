class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}

        for i in s:
            if i not in check:
                check[i] = 1

            else:
                check[i] += 1

        print(check)

        for i in t:
            if i in check:
                check[i] -= 1
                continue

            else:
                return False

        
        for i in check.values():
            if i != 0:
                return False

        return True
