class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)

        closest = abs(target - (nums[0] + nums[1] + nums[2]))
        output = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                
                temp = nums[i] + nums[j] + nums[k]
                #print(nums[i], nums[j], nums[k], temp, closest, abs(target-temp))
                if abs(target - temp) == 0:
                    return temp
                if abs(target - temp) < closest:
                    closest = abs(target - temp)
                    output = temp


                if temp > target:
                    k -= 1

                else:
                    j += 1

        return output