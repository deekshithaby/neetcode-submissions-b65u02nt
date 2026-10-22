class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(numbers):
            needed = target - num

            if needed in num_map:
                return [num_map[needed]+1, i+1]

            num_map[num] = i
