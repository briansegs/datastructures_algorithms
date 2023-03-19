class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums


solution1 = Solution()
solution2 = Solution()

print(solution1.getConcatenation([1,2,1]))

print(solution2.getConcatenation([1,3,2,1]))