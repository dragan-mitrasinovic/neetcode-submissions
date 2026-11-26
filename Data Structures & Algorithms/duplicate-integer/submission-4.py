class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements_appeared = set()

        for num in nums:
            if num in elements_appeared:
                return True
            
            elements_appeared.add(num)
        
        return False