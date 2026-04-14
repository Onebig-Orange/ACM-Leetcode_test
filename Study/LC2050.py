# LeetCode 2050. 并行课程 III
# 题目描述：给定一个正整数 n（课程编号 1 到 n）和一个数组 relations，
#          其中 relations[i] = [prevCourse, nextCourse] 表示课程 prevCourse
#          必须在课程 nextCourse 之前完成（即有向边：prevCourse → nextCourse）。
#          另给定一个数组 time，其中 time[i] 表示完成第 i 门课程所需的时间。
#          返回完成所有课程所需的最少时间。
# 难度：Hard（拓扑排序 + 动态规划）

import sys
from typing import List
from collections import defaultdict, deque

# ================= 核心算法部分 =================
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        解题思路：拓扑排序 + 动态规划
        
        核心观察：
        - 课程之间有依赖关系，构成一个 DAG（有向无环图）
        - 课程的最早完成时间 = 所有前置课程完成时间中的最大值 + 当前课程时间
        
        动态规划公式：
        dp[i] = max(dp[所有前置课程]) + time[i]
        
        其中 dp[i] 表示完成课程 i 的最早时间
        
        算法步骤：
        1. 建立邻接表和入度数组
        2. 用队列进行拓扑排序
        3. 在拓扑排序过程中，用 dp 记录每个课程的最早完成时间
        4. 最终答案是所有 dp 中的最大值
        """
        
        # ========== 第一步：建立图结构 ==========
        # 邻接表：adj[i] 存储课程 i 指向的所有后续课程
        adj = defaultdict(list)
        
        # 入度数组：in_degree[i] 表示课程 i 的前置课程数量
        # 即有多少条边指向课程 i
        in_degree = [0] * (n + 1)  # 索引 0 不使用
        
        # 处理所有边的关系
        for prev_course, next_course in relations:
            # 从 prev_course 指向 next_course
            adj[prev_course].append(next_course)
            # next_course 的入度加一
            in_degree[next_course] += 1
        
        # ========== 第二步：初始化 dp ==========
        # dp[i] 表示完成课程 i 的最早时间
        # 初始化为当前课程的时间（没有前置课程的情况）
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = time[i - 1]  # time 数组是 0-indexed
        
        # ========== 第三步：拓扑排序 + DP ==========
        # 将所有入度为 0 的课程加入队列（没有前置课程，可以直接开始）
        queue = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 当队列非空时，说明还有课程可以学习
        while queue:
            # 取出当前可以学习的课程
            curr = queue.popleft()
            
            # 遍历当前课程的所有后续课程
            for next_course in adj[curr]:
                # 更新后续课程的最早完成时间
                # 必须等所有前置课程都完成，所以取 max
                dp[next_course] = max(dp[next_course], dp[curr] + time[next_course - 1])
                
                # 减少后续课程的入度（相当于删除了这条边）
                in_degree[next_course] -= 1
                
                # 如果后续课程的所有前置课程都已完成，加入队列
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # ========== 第四步：返回答案 ==========
        # 所有课程都完成后的总时间 = 完成时间最长的课程
        return max(dp[1:])  # dp[1:] 忽略索引 0


# ================= 另一种实现：手动模拟递归（DFS + 记忆化） ==========
class Solution_DFS:
    """
    深度优先搜索 + 记忆化搜索
    
    思路：
    - 对于每个课程，递归计算其所有前置课程的最大完成时间
    - 使用记忆化避免重复计算
    
    时间复杂度：O(N + E)，其中 E 是边的数量
    空间复杂度：O(N + E)
    """
    
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # 建立反向邻接表：rev_adj[i] 存储所有指向 i 的前置课程
        rev_adj = [[] for _ in range(n + 1)]
        for prev, nxt in relations:
            rev_adj[nxt].append(prev)
        
        # dp 数组用于记忆化，-1 表示未计算
        dp = [-1] * (n + 1)
        
        def dfs(course: int) -> int:
            """
            递归计算完成课程 course 的最早时间
            
            返回值：完成该课程所需的最短时间
            """
            # 如果已经计算过，直接返回
            if dp[course] != -1:
                return dp[course]
            
            # 如果没有前置课程，完成时间就是当前课程的时间
            if not rev_adj[course]:
                dp[course] = time[course - 1]
                return dp[course]
            
            # 否则，递归计算所有前置课程的最大完成时间
            max_prereq_time = 0
            for prereq in rev_adj[course]:
                # 取所有前置课程完成时间的最大值
                max_prereq_time = max(max_prereq_time, dfs(prereq))
            
            # 当前课程的最早完成时间 = max(前置课程时间) + 当前课程时间
            dp[course] = max_prereq_time + time[course - 1]
            return dp[course]
        
        # 计算每门课程的最早完成时间，取最大值
        result = 0
        for i in range(1, n + 1):
            result = max(result, dfs(i))
        
        return result


# ================= ACM 本地输入输出处理部分 =================
if __name__ == "__main__":
    # 读取所有输入数据
    input_data = sys.stdin.read().split()
    
    if not input_data:
        sys.exit()
    
    # 输入格式：
    # 第一行：n（课程数量）
    # 第二行：m（关系数量）
    # 第三行：n 个整数，表示每门课程的完成时间
    # 接下来 m 行：每行两个整数 [prevCourse, nextCourse]
    # 
    # 示例：
    # 3
    # 2
    # 3 2 3
    # 1 2
    # 1 3
    
    ptr = 0
    n = int(input_data[ptr]); ptr += 1
    m = int(input_data[ptr]); ptr += 1
    
    time = [int(input_data[ptr + i]) for i in range(n)]; ptr += n
    
    relations = []
    for _ in range(m):
        relations.append([int(input_data[ptr]), int(input_data[ptr + 1])])
        ptr += 2
    
    # 实例化调用
    sol = Solution()
    result = sol.minimumTime(n, relations, time)
    
    # 打印结果
    print(result)

# ================= 测试用例 =================
# 示例 1:
# n = 3, m = 2
# time = [3, 2, 3]
# relations = [[1,2], [1,3]]
# 
# 课程图：
#     1 (3)
#    / \
#   2   3
#  (2) (3)
#
# 分析：
# - 课程1: 无前置，完成时间 = 3
# - 课程2: 前置是1，完成时间 = 3 + 2 = 5
# - 课程3: 前置是1，完成时间 = 3 + 3 = 6
# - 总时间 = max(3, 5, 6) = 6
#
# 输出: 6
#
# 示例 2:
# n = 5, m = 4
# time = [1, 2, 3, 4, 5]
# relations = [[1,5], [2,5], [3,5], [4,5]]
#
# 课程图：
#   1 2 3 4
#    \|/|
#     5
#
# 分析：
# - 课程1,2,3,4 都无前置，分别需要 1,2,3,4 天
# - 课程5 必须等 1,2,3,4 都完成，完成时间 = 4 + 5 = 9
#
# 输出: 9
