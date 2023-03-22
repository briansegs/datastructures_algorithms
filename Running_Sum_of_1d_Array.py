class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rs = []

        for n in nums:
            if rs:
                rs.append(n + rs[-1])
            else:
                rs.append(n)
        return rs

def test_solutions():
    solution = Solution()

    assert solution.runningSum([]) == [], "should be []"
    assert solution.runningSum([1,2,3,4]) == [1,3,6,10], "should be [1,3,6,10]"
    assert solution.runningSum([1,1,1,1,1]) == [1,2,3,4,5], "should be [1,2,3,4,5]"
    assert solution.runningSum([3,1,2,10,1]) == [3,4,6,16,17], "should be [3,4,6,16,17]"

if __name__ == "__main__":
    test_solutions()
    print("everything passed")