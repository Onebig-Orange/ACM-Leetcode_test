import sys

def three_sum(nums):
    """返回所有不重复的三元组，每个三元组内数字升序"""
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 2):
        # 跳过重复的起始元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        target = -nums[i]
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                res.append([nums[i], nums[left], nums[right]])
                # 跳过重复的 left 和 right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return res

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    nums = list(map(int, data))
    result = three_sum(nums)
    out_lines = []
    for triplet in result:
        out_lines.append(f"{triplet[0]} {triplet[1]} {triplet[2]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()