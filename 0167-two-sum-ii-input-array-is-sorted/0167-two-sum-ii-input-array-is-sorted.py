class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        j=len(numbers)-1
        i=0
        while i<j:
            sum=numbers[i]+numbers[j]
            if sum==target:
                return[i+1,j+1]
            elif sum<target:
                i=i+1
            else:
                j=j-1
                
            


                
                    
                    