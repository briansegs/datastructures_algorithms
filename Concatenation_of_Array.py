class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums


solution1 = Solution()
solution2 = Solution()

def test_solutions():
    assert solution1.getConcatenation([1,2,1]) == [1, 2, 1, 1, 2, 1], "Should be [1, 2, 1, 1, 2, 1]"
    assert solution2.getConcatenation([1,3,2,1]) == [1, 3, 2, 1, 1, 3, 2, 1], "Should be [1, 3, 2, 1, 1, 3, 2, 1]"

if __name__ == "__main__":
    test_solutions()
    print("Everything passed")