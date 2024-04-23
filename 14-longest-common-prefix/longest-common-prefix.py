class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if '' in strs:
            return ''
        pref = ''

        common = True
        count = 0

        while common:
            if len(strs[0]) == count:
                return pref
            pref += strs[0][count]

            for i in strs:
                if not i.startswith(pref):
                    return pref[:-1]

            count += 1

        return pref