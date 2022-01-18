class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # 相加创建新数组后，进行排序（这里用冒泡，应该有更快的）
        sum = 0
        height = [0]
        for i in gain:
            sum += i
            height.append(sum)
        
        
        for i in range(1,len(height)):
            for j in range(0,len(height)-i):
                if height[j] > height[j+1]:
                    height[j],height[j+1] = height[j+1],height[j]
        highest = height[len(height)-1]
        return highest

Success
Details 
Runtime: 40 ms, faster than 14.01% of Python online submissions for Find the Highest Altitude.
Memory Usage: 13.8 MB, less than 12.56% of Python online submissions for Find the Highest Altitude.