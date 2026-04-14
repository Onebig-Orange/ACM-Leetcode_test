# LeetCode 347. 前 K 个高频元素
# 题目描述：给定一个整数数组 nums 和一个整数 k，返回其中出现频率最高的 k 个元素。
#          返回的答案可以按任意顺序返回。
# 示例：nums = [1,1,1,2,2,3], k = 2 → 输出: [1,2] 或 [2,1]

import sys
import heapq
from typing import List
from collections import Counter

# ================= 核心算法部分 =================
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        使用堆排序的思想解决 Top K 问题
        
        解题思路：
        1. 第一步：统计每个数字出现的频率 - 使用哈希表（字典）
        2. 第二步：建立大小为 k 的最小堆
           - 堆中存储 (频率, 数字) 元组
           - 最小堆的堆顶是最小值，方便我们淘汰低频元素
        3. 遍历所有数字，当堆大小超过 k 时，弹出堆顶（淘汰低频元素）
        4. 最终堆中就是频率最高的 k 个元素
        
        为什么用最小堆而不是最大堆？
        - 如果用最大堆，我们需要把 n 个元素全部加入堆中，复杂度 O(n log n)
        - 用最小堆，只需维护 k 个元素，复杂度 O(n log k)，更优
        """
        
        # ========== 第一步：统计频率 ==========
        # Counter 是一个方便的计数器，统计每个元素出现的次数
        # 例如：[1,1,2,2,2,3] → {1:2, 2:3, 3:1}
        freq_counter = Counter(nums)
        
        # ========== 第二步：建立最小堆 ==========
        # heapq 是 Python 的最小堆实现
        # 我们需要建立大小为 k 的最小堆来维护 Top K
        
        # min_heap: 存储 (频率, 数字) 元组
        # Python 的 heapq 是最小堆，所以频率小的会在堆顶
        min_heap = []
        
        # 遍历每个数字及其频率
        for num, freq in freq_counter.items():
            # 将 (频率, 数字) 推入堆中
            heapq.heappush(min_heap, (freq, num))
            
            # 当堆的大小超过 k 时，需要弹出堆顶
            # 因为堆顶是最小频率的元素，弹出它可以保持堆中都是高频元素
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # ========== 第三步：提取结果 ==========
        # 注意：虽然堆中维护的是 Top K，但我们只需要返回数字本身
        # 遍历堆，取出所有数字
        result = []
        for freq, num in min_heap:
            result.append(num)
        
        return result


# ================= 另一种解法：桶排序 ==========
class Solution_BucketSort:
    """
    桶排序解法 - 空间换时间
    
    思路：
    - 最大频率 = len(nums)，创建 len(nums)+1 个桶
    - 桶的索引 = 频率，存储该频率的所有数字
    - 从后往前（高频到低频）收集 k 个元素
    """
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 第一步：统计频率
        freq_counter = Counter[int](nums)
        
        # 第二步：创建频率桶
        # buckets[i] 存储出现 i 次的所有数字
        # 频率范围是 1 ~ len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_counter.items():
            buckets[freq].append(num)
        
        # 第三步：从高频桶开始收集
        result = []
        for freq in range(len(nums), 0, -1):
            result.extend(buckets[freq])
            # 收集够 k 个就停止
            if len(result) >= k:
                break
        
        return result[:k]


# ================= ACM 本地输入输出处理部分 =================
if __name__ == "__main__":
    # 读取所有输入数据
    input_data = sys.stdin.read().split()
    
    # 如果没有输入，直接退出
    if not input_data:
        sys.exit()
    
    # 约定输入格式：
    # 第一行：数组长度 n 和 k
    # 第二行：n 个整数（数组元素）
    # 例如：
    # 6 2
    # 1 1 1 2 2 3
    
    n = int(input_data[0])
    k = int(input_data[1])
    nums = [int(x) for x in input_data[2:2+n]]
    
    # 实例化调用
    sol = Solution()
    result = sol.topKFrequent(nums, k)
    
    # 打印结果（用空格分隔）
    print(' '.join(map(str, result)))

# ================= 测试用例 =================
# 示例 1:
# 输入: 6 2 / 1 1 1 2 2 3
# 输出: 1 2 或 2 1
# 解释: 1出现3次，2出现2次，3出现1次，所以1和2是出现频率最高的两个元素
#
# 示例 2:
# 输入: 5 1 / 1
# 输出: 1
# 解释: 唯一元素
#
# 示例 3:
# 输入: 7 2 / 1 1 1 2 2 3 3
# 输出: 1 2 或 1 3 或 2 3（任选两个出现2次以上的）
# 解释: 1出现3次，2和3各出现2次
