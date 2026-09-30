class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        h = n - 1
        while h >= l:
            middle = (h + l) // 2
            if nums[middle] == target:
                return True
            elif nums[l] == nums[middle] == nums[h]:
                l = l + 1
                h = h - 1
                continue
            elif nums[middle] <= nums[h]:
                if nums[middle] <= target <= nums[h]:
                    l = middle + 1
                else:
                    h = middle - 1
            else:
                if nums[l] <= target <= nums[middle]:
                    h = middle - 1
                else:
                    l = middle + 1
        return False
