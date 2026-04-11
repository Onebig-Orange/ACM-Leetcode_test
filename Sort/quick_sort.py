# 快速排序
import sys
import random
from typing import List

class Solution:
    def sortArry(self, nums: List[int]) -> List[int]:
        def quick_sort(left, right):
            if left >= right:
                return
            mid_index = random.randint(left, right)
            nums[left], nums[mid_index] = nums[mid_index], nums[left]
            mid = nums[mid_index]
            i, j = left, right
            while i < j:
                while i < j and nums[j] >= mid:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= mid:
                    i += 1
                nums[j] = nums[i]
            nums[i] = mid

        quick_sort(0, len(nums) - 1)
        return nums

if __name__=="__main__":
    input_data = sys.stdin.read().split()

    if not input_data:
        sys.exit()

    nums = [int(x) for x in input_data]

    sol = Solution()
    res = sol.sortArry(nums)

    print(*(res)) 