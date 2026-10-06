class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        def twr(l, r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l = l + 1
                r = r - 1

        twr(0, n - 1)
        twr(0, k - 1)
        twr(k, n - 1)