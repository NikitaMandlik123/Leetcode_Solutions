class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for arr in image:
            i=0
            j=len(arr)-1
            while(i<j):
                arr[i],arr[j]=arr[j],arr[i]
                arr[i]=arr[i]^1
                arr[j]=arr[j]^1
                i+=1
                j-=1
            if(len(arr)&1==1):
                arr[i]=arr[i]^1
        return image
    
    #TC = O(n^2)
    #SC = O(1)
    