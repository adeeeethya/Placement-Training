#leet713
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        r,l,p=0,0,1
        length=0
        if k<=1:
            return 0
        while (r<len(nums)):
            p=p*nums[r]
            while p>=k:
                p=p//nums[l]
                l=l+1
            length+=r-l+1
            
            r=r+1
        return length
