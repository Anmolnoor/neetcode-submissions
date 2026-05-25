class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length= len(nums)
        for r in range(length):
            for x in range(r +1, length):
                if  nums[r] + nums[x] == target:
                    return [r, x]
