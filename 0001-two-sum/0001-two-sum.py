class Solution(object):
    def twoSum(self, nums, target):
        visited = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in visited:
                return [visited[rem], i]
            visited[num] = i
        