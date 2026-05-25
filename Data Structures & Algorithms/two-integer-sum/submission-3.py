class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length= len(nums)
        for r in range(length):
            required = target - nums[r]
            for x in range(r +1, length):
                if required == nums[x]:
                    return [r, x]
