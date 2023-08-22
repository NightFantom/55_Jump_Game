from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_index = len(nums) - 1
        achieved_pos = min(nums[0], right_index)
        index = 0
        while index < achieved_pos:
            index += 1
            distant_pos = nums[index] + index
            if distant_pos > achieved_pos:
                achieved_pos = min(distant_pos, right_index)
                if achieved_pos == right_index:
                    index = achieved_pos
        return index == right_index
