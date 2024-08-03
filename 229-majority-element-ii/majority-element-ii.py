class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elements = {}

        for i in nums:
            if i in elements:
                elements[i] += 1

            else:
                elements[i] = 1

        print(elements)

        length = (len(nums)/3)
        print(length)
        majority = []

        for i in elements:
            if elements[i] > length:
                majority.append(i)

        return majority