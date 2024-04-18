class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr1, arr2 = 0, 0
        
        merged = []
        
        while nums1 or nums2:
            if not nums2:
                merged.append(nums1.pop(0))
                
            elif not nums1:
                merged.append(nums2.pop(0))
                
            elif nums1[0] > nums2[0]:
                merged.append(nums2.pop(0))

            else:
                merged.append(nums1.pop(0))

        print(merged)    
        if len(merged) % 2 != 0: #num is odd
            median = merged[int(len(merged)/2)]
            
            
        else:
            print(type(int(len(merged)/2 - 1)))
            median = (merged[int(len(merged)/2 - 1)] + merged[int(len(merged)/2)]) /2
            print(median)
        return median