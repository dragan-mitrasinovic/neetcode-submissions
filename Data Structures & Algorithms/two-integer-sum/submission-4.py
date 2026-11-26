class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appeared_at = {}

        for index, num in enumerate(nums):
            match = target - num
            if match in appeared_at:
                return [appeared_at[match], index]
            
            appeared_at[num] = index
        
        return [-1, -1]