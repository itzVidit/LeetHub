class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n= len(nums)
        result = set()
        for i in range(0,n):
            my_set=set()
            for j in range(i+1,n):
                rem = - (nums[i]+nums[j])
                if rem in my_set:
                    temp = [nums[i],nums[j],rem]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])
        return [list(ans) for ans in result ]
        