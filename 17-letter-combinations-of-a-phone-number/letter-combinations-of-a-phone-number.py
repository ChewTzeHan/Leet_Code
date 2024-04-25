class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return

        combo = []

        letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
        ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v',],
        ['w', 'x', 'y', 'z']]

        iterations = [0 for i in digits]
        letter_index = [(int(i) - 2) for i in digits]
        last_num = []
        for i in letter_index:
            last_num.append(len(letters[i]) - 1)
        print(last_num)
        
        print(iterations)
        print(letter_index)

        
        while iterations:
            print('start')
            print(iterations)
            num = ''
            for i in range(len(letter_index)):
                num += letters[letter_index[i]][iterations[i]]
            combo.append(num)

            if iterations == last_num:
                print('exit')
                break
            iterations[-1] += 1
            print(iterations)
            print('end')
            
            
            for i in range(1, len(iterations) + 1):
                if iterations[-i] >= 3:
                    if letter_index[-i] == 5 or letter_index[-i] == 7:
                        if iterations[-i] >= 4:
                            iterations[-i-1] += 1
                            iterations[-i] = 0
                            continue
                    
                    else:
                            iterations[-i-1] += 1
                            iterations[-i] = 0



        return combo