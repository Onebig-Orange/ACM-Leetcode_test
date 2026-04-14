# LeetCode 121. 买卖股票的最佳时机
# 题目描述：给定一个数组 prices，prices[i] 表示第 i 天的股票价格。
#          你只能选择某一天买入，然后在未来的某一天卖出。
#          求能够获取的最大利润。如果无法获取利润则返回 0。
# 示例：prices = [7,1,5,3,6,4] → 最大利润 = 5（买入价 1，卖出价 6）

import sys
from typing import List

# ================= 核心算法部分 =================
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        使用贪心算法求解最大利润
        
        核心思想：
        - 在遍历过程中，实时记录当前为止的最低价格（最小买入价）
        - 在遍历过程中，计算以当前最低价格买入、今天卖出的利润
        - 取所有利润的最大值
        
        为什么这样做是对的？
        - 假设最大利润发生在第 i 天买入、第 j 天卖出（i < j）
        - 那么第 i 天的价格一定是 0~i 天中的最低价格
        - 所以我们只需要记录历史最低价格，就能找到最优解
        """
        
        # 边界情况：没有价格数据或只有一天，无法交易
        if not prices or len(prices) < 2:
            return 0
        
        # min_price: 截至当前天数的最低股票价格
        # 初始化为第一天的价格
        min_price = prices[0]
        
        # max_profit: 截至目前获得的最大利润
        # 初始化为 0（至少不交易）
        max_profit = 0
        
        # 从第二天开始遍历（索引 1 开始）
        for i in range(1, len(prices)):
            # 1. 更新历史最低价格
            #    如果今天价格更低，说明找到了更便宜的买入时机
            if prices[i] < min_price:
                min_price = prices[i]
            
            # 2. 计算以历史最低价格买入、今天卖出的利润
            profit = prices[i] - min_price
            
            # 3. 更新最大利润
            #    如果今天卖出的利润更大，则更新
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

# ================= ACM 本地输入输出处理部分 =================
if __name__ == "__main__":
    # 读取所有输入数据
    input_data = sys.stdin.read().split()
    
    # 如果没有输入，直接退出
    if not input_data:
        sys.exit()
    
    # 将输入转换为整数数组（每一天的股票价格）
    prices = [int(x) for x in input_data]
    
    # 实例化 Solution 并调用算法
    sol = Solution()
    result = sol.maxProfit(prices)
    
    # 打印结果
    print(result)

# ================= 测试用例 =================
# 输入: 7 1 5 3 6 4
# 输出: 5
# 解释: 在第2天买入(价格=1)，第5天卖出(价格=6)，利润 = 6-1 = 5
#
# 输入: 7 6 4 3 1
# 输出: 0
# 解释: 股票价格持续下跌，任何交易都会亏损，所以选择不交易
