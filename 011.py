class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time: O(N^2)
        # Result: TLE
        """
        n = len(height)
        Max_area = float('-INF')
        
        for left in range(n):
            for right in range(left+1,n):
                area = (right - left)*min(height[left], height[right])
                Max_area = max(area, Max_area)
        return Max_area
        """

        # Time: O(N)
        # Result: ACCEPT
        # Concept: Move the right one will decrease the area (w-1)*H_left, 
        #          so it's not necessary to consider the right one larger than left one.
        Max_area = float('-INF')
        left = 0
        right = len(height)-1
        
        while left < right: 
            area = (right - left)*min(height[left], height[right])
            Max_area = max(area, Max_area)layout
            
            if(height[left] < height[right]):
                left+=1
            else:
                right-=1
        
        return Max_area
