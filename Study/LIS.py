import sys
import bisect

# 读取所有输入，按空白分割，并转换为整数列表
data_in = list(map(int, sys.stdin.read().strip().split()))

class Solution:
    def LIS_with_path(self, nums):   # 加上 self 参数
        dp = []
        pos = [0] * len(nums)

        for i, x in enumerate(nums):
            p = bisect.bisect_left(dp, x)
            if p == len(dp):
                dp.append(x)
            else:
                dp[p] = x
            pos[i] = p

        length = len(dp)
        lis = []
        curr_len = length - 1
        for i in range(len(nums) - 1, -1, -1):
            if pos[i] == curr_len:
                lis.append(nums[i])
                curr_len -= 1
                if curr_len < 0:
                    break
        return lis[::-1]

sol = Solution()
res = sol.LIS_with_path(data_in)   # 调用实例方法
print(*res)                        # 输出序列，空格分隔