class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 1
        n = 1
        for _ in range(len(nums)-1):
            if nums[n] > nums[cur-1]:
                nums[cur], nums[n] = nums[n], nums[cur]
                cur += 1
                n += 1
            else:
                n += 1
        return cur