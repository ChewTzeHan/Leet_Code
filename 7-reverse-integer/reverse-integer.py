class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return x

        def int_range(x):
            if int(x) > (pow(2, 31) - 1):
                return 0
            elif int(x) < -(pow(2, 31)):
                return 0

            else:
                return x

        if x < 1:
            string_int = int_range(str(abs(x))[::-1])
            
            return -int(string_int)
        
        else:
            string_int = int_range(str(abs(x))[::-1])
            return int(string_int)


        
