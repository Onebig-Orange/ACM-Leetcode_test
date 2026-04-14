# LCR 076 数组中的第 K 个最大元素 快速选择
import sys
import random
from typing import List

# ================= 核心算法部分 =================
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 第 k 大的元素，在升序数组中的索引位置应该是 len(nums) - k
        target_idx = len(nums) - k
        
        def quick_select(left: int, right: int) -> int:
            # 1. 随机选基准，防止极端测试用例导致时间复杂度退化为 O(N^2)
            pivot_idx = random.randint(left, right)
            nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
            pivot = nums[left]
            
            # 2. 双指针划分（和快排完全一样）
            i, j = left, right
            while i < j:
                while i < j and nums[j] >= pivot: 
                    j -= 1
                nums[i] = nums[j]
                
                while i < j and nums[i] <= pivot: 
                    i += 1
                nums[j] = nums[i]
                
            nums[i] = pivot
            
            # 3. 核心分支：判断当前确定的位置是不是我们要找的靶心
            if i == target_idx:
                return nums[i]          # 命中靶心，直接返回！
            elif i < target_idx:
                return quick_select(i + 1, right)  # 目标在右半边，只需递归右边
            else:
                return quick_select(left, i - 1)   # 目标在左半边，只需递归左边

        return quick_select(0, len(nums) - 1)

# ================= ACM 本地输入输出处理部分 =================
if __name__ == "__main__":
    # 一次性读取所有的输入字符，按空白（空格/换行）分割成列表
    input_data = sys.stdin.read().split()
    
    # 如果没读到数据，直接退出
    if not input_data:
        sys.exit()
    
    # 根据这道题的输入习惯：最后 1 个数字是 k，前面所有的数字是 nums 数组
    k = int(input_data[-1])
    nums = [int(x) for x in input_data[:-1]]
    
    # 实例化调用
    sol = Solution()
    res = sol.findKthLargest(nums, k)
    
    # 打印最终结果
    print(res)
