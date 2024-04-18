class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    if (nums[i] + nums[j]) == target:
                        ans = [i, j]
                        break
            if ans != []:
                break
        return ans
            
        


