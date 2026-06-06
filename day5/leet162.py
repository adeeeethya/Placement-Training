class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)-1
        if n==0:
            return 0
        elif nums[0]>nums[1]:
            return 0
        elif nums[-1]>nums[-2]:
            return n
        #code till now is for peak at first element and peak at last element
        #case1 mid at peak
        #case2 mid at left slope
        #case3 mid at right slope
        
        s,e=1,n-1
        while s<=e:
            m=(s+e)//2
            if nums[m-1]<nums[m]>nums[m+1]:
                return m
            elif nums[m]<nums[m+1]: #peak is at right side
                s=m+1
            else: #peak is at left side
                e=m-1

        