class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for i in s:
            if i.isalpha() or i.isdigit():
                new += i

        new = new.lower()



        print(new)

        if len(new) == 1:
            return True
        p1, p2 = 0, -1

        while p1 != len(new):
            if new[p1] == new[p2]:
                p1 += 1
                p2 -= 1
                continue

            else:
                return False

        return True