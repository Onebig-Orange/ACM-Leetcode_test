# 归并排序
import sys
from typing import List

class Solution():
    def sortArry(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])

            return merge(left_half, right_half)

        def merge(nums_left, nums_right):
            merged = []
            i = j = 0

            while i < len(nums_left) and j < len(nums_right):
                if nums_left[i] <= nums_right[j]:
                    merged.append(nums_left[i])
                    i += 1
                else:
                    merged.append(nums_right[i])
                    j += 1
            
            merged.extend(nums_left[i:])
            merged.extend(nums_right[j:])
            return merged

        return merge_sort(nums)

if __name__=="__main__":
    input_data = sys.stdin.read().split()

    if not input_data:
        sys.exit

    nums = [x for x in input_data]
    sol = Solution()
    res = sol.sortArry(nums)

    print(*res)

