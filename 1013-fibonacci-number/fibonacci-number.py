class Solution:
    def fib(self, n: int) -> int:
        
        return find_fib(n)

def find_fib(n):
    if n == 1:
        return 1

    elif n == 0:
        return 0

    else:
        return find_fib(n-1) + find_fib(n-2)