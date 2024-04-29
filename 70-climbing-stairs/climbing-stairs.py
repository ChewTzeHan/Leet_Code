class Solution:
    def climbStairs(self, n: int) -> int:

        if n == (0 or 1):
            return 1

        memory = [0] * (n+1)
        memory[0] = memory[1] = 1
        print(memory)

        for i in range(2, n+1):
            memory[i] = memory[i-1] + memory[i-2]

        print(memory)

        return memory[n]