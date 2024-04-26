class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []

            if not nums:
                return result

            average = target // k

            if average < nums[0] or nums[-1] < average:
                return result

            if k == 2:
                return twoSum(nums, target)

            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i+1:], target - nums[i], k - 1):
                        #print(subset)
                        result.append([nums[i]] + subset)

            return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            low, high = 0, len(nums) - 1

            while low < high:
                temp = nums[low] + nums[high]
                if temp < target or (low > 0 and nums[low] == nums[low - 1]):
                    low += 1

                elif temp > target or (high < len(nums) - 1 and nums[high] == nums[high + 1]):
                    high -= 1

                else:
                    result.append([nums[low], nums[high]])
                    high -= 1
                    low += 1

            return result

        return kSum(nums, target, 4)