# LCR 078. 合并 K 个升序链表
# 题目描述：给定一个数组 lists，里面存放了 K 个升序链表的头节点，将这 K 个升序链表合并为一个升序链表并返回。

import sys
import heapq
from typing import Optional, List

# ================= 链表节点定义 =================
class ListNode:
    """链表节点定义"""
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val      # 节点的值
        self.next = next     # 指向下一个节点的指针

# ================= 核心算法部分 =================
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 使用最小堆（PriorityQueue）来高效找到所有链表头部中的最小值
        # 堆中存储格式：(节点值, 链表索引, 节点对象)
        # 注意：加入索引是为了处理节点值相同的情况，避免 ListNode 对象无法比较的问题

        # 1. 初始化最小堆，将每个链表的头节点加入堆中
        heap = []
        for i, node in enumerate(lists):
            if node:
                # 将 (节点值, 索引, 节点) 放入堆中
                heapq.heappush(heap, (node.val, i, node))

        # 2. 创建哑节点(dummy)，作为合并后链表的头部的前一个节点
        # 这样可以统一处理，避免单独处理头节点的特殊情况
        dummy = ListNode(0)
        current = dummy  # current 指针用于构建新链表

        # 3. 循环取出堆中最小的节点，直到堆为空
        while heap:
            # 弹出堆顶元素（值最小的节点）
            val, i, node = heapq.heappop(heap)

            # 将弹出的节点接到结果链表的末尾
            current.next = node
            current = current.next

            # 4. 如果该节点还有下一个节点，将下一个节点加入堆中
            # 这是因为每个链表都是升序的，所以下一个节点有可能是全局最小的
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        # 5. 返回哑节点的下一个节点，即合并后链表的头节点
        return dummy.next

# ================= ACM 本地输入输出处理部分 =================
if __name__ == "__main__":
    # 读取所有输入数据
    input_data = sys.stdin.read().split()

    # 如果没有输入，直接退出
    if not input_data:
        sys.exit()

    # 由于是链表输入，我们约定：
    # 第一行 K 表示链表的个数
    # 接下来 K 行，每行是一个链表的节点值（用空格分隔），-1 表示该链表结束
    # 例如：
    # 3
    # 1 4 5 -1
    # 1 3 4 -1
    # 2 6 -1

    ptr = 0
    k = int(input_data[ptr])
    ptr += 1

    lists = []
    for _ in range(k):
        nodes = []
        while ptr < len(input_data) and input_data[ptr] != '-1':
            nodes.append(int(input_data[ptr]))
            ptr += 1
        ptr += 1  # 跳过 -1

        # 将节点值数组转换为链表
        dummy = ListNode(0)
        current = dummy
        for val in nodes:
            current.next = ListNode(val)
            current = current.next
        lists.append(dummy.next)

    # 实例化调用
    sol = Solution()
    result = sol.mergeKLists(lists)

    # 打印结果链表的值
    output = []
    while result:
        output.append(str(result.val))
        result = result.next
    output.append('-1')  # 以 -1 结束

    print(' '.join(output))
