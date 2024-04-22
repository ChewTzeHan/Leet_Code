class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = height[0], height[-1]
        left_ind, right_ind = 0, -1

        length = len(height) - 1

        max_area = 0

        while (left_ind + abs(right_ind)) != len(height):
            area = min(left, right) * length
            if area > max_area:
                max_area = area

            length -= 1
            if left < right:
                left_ind += 1
                left = height[left_ind]

            else:
                right_ind -= 1
                right = height[right_ind]

        return max_area