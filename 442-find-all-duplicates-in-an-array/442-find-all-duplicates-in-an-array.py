class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
            nums.sort()
            n= len(nums)
            p1=0
            p2=1
            ans=[]
            for i in range(0,n-1):
                if nums[p1]==nums[p2]:
                    ans.append(nums[p2])
                else:
                    p1=p2
                p2+=1
            return ans
           
            
    #time complexity : O(n)
    #space complexity: O(1)
            
            
        