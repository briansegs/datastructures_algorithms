class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums


def test_solutions():
    solution = Solution()

    assert solution.getConcatenation([]) == [], "Should be []"
    assert solution.getConcatenation([1,2,1]) == [1, 2, 1, 1, 2, 1], "Should be [1, 2, 1, 1, 2, 1]"
    assert solution.getConcatenation([1,3,2,1]) == [1, 3, 2, 1, 1, 3, 2, 1], "Should be [1, 3, 2, 1, 1, 3, 2, 1]"


if __name__ == "__main__":
    test_solutions()
    print("Everything passed")