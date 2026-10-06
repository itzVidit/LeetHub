class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        m = {}

        for num in nums:
            m[num] = m.get(num,0) + 1

        n = n//2
        for key,value in m.items():
            if value > n:
                return key
        return 0
            
        