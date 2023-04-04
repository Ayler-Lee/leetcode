class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(head, tail):
            while head < tail:
                nums[head], nums[tail] = nums[tail], nums[head]
                head += 1
                tail -= 1

        k = k % len(nums)

        reverse(0, len(nums) - 1 - k)
        reverse(len(nums) - k, len(nums) - 1)
        reverse(0, len(nums) - 1)
        
        return nums

for i in range(1, 3, 2):
    print(i)