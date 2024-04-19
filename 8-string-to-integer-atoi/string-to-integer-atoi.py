class Solution:
    def myAtoi(self, s: str) -> int:
        num_str = ''

        if s == '':
            return 0

        neg = False
        opp_found = False

        for i in s.strip():
            if i.isnumeric() == False:
                if i == '-' and opp_found == False:
                    
                    if num_str != '':
                        break
                    neg = True
                    opp_found = True
                    continue

                elif i == '+' and opp_found == False:
                    
                    if num_str != '':
                        break
                    neg = False
                    opp_found = True
                    continue

                else:
                    break

            elif i.isnumeric():
                num_str += i

            

        if num_str == '':
            return 0

        print(num_str)
        if neg == True and int(num_str) > pow(2, 31) - 1:
            return -pow(2, 31)

        elif int(num_str) > (pow(2 , 31) - 1):
            return pow(2, 31) - 1
        

        if neg == True:
            return -int(num_str)
        else:
            return int(num_str)



        
