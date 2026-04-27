class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxi = 0

        for num in nums:
            if num - 1 not in nums:
                elem = num
                count = 1   # 🔥 reset here

                while elem + 1 in nums:
                    elem += 1
                    count += 1

                maxi = max(maxi, count)

        return maxi