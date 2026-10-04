class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        lm=height[l]
        rm=height[r]
        w=0
        while l<r:
            if lm<rm:
                l+=1
                lm=max(lm,height[l])
                w+=lm-height[l]
            else:
                r-=1
                rm=max(rm,height[r])
                w+=rm-height[r]
        return w