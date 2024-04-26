class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = len(s) - 1, len(p) - 1
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, cache, s, p, i, j):
        print('cache:', cache)
        key = (i, j)
        print('key:', key)
        if key in cache:
            return cache[key]

        if i == -1 and j == -1:
            cache[key] = True
            return True

        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]

        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            
            if k == -1:
                cache[key] = True
                return cache[key]
            
            cache[key] = False
            return cache[key]
        
        if i == -1 and p[j] != '*':
            cache[key] = False
            return cache[key]

        if p[j] == '*':
            if self.backtrack(cache, s, p, i, j - 2):
                cache[key] = True
                return cache[key]
            
            if p[j - 1] == s[i] or p[j - 1] == '.':
                if self.backtrack(cache, s, p, i - 1, j):
                    cache[key] = True
                    return cache[key]
        
        if p[j] == '.' or s[i] == p[j]:
            if self.backtrack(cache, s, p, i - 1, j - 1):
                cache[key] = True
                return cache[key]

        cache[key] = False
        return cache[key]

        '''
        memory = ''
        
        count = 20
        while s:
            print(s, p, memory)
            
            count -= 1
            if count < 0:
                break

            if len(s) > 0 and len(p) == 0 and (memory == '' or (memory != s[-1] and memory != '.')):
                return False


            if len(p) > 0:
                if s[-1] == p[-1]:
                    s = s[:-1]
                    p = p[:-1]
                    memory = ''
                    continue
                
                elif p[-1] == '.':
                    s = s[:-1]
                    p = p[:-1]
                    continue

            if s[-1] == memory or memory == '.':
                s = s[:-1]
                continue

            if len(p) > 1:
                if p[-1] == '*':
                    memory = p[-2]
                    p = p[:-2]
                    continue

            return False
            
        print('looped')
        print(s, p)
        if s == '' and p == '':
            return True
        
        elif len(p) > 1:
            while p:
                if p[-1] == '*':
                    p = p[:-2]
                elif p[-1] == memory:
                    p = p[:-1]
                else:
                    return False
            return True

        
        else:
            return False
        '''
