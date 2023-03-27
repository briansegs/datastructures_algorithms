class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans

def test_solutions():
    solutions = Solution()

    assert solutions.buildArray([]) == [], "should be []"
    assert solutions.buildArray([0,2,1,5,3,4]) == [0,1,2,4,5,3], "should be [0,1,2,4,5,3]"
    assert solutions.buildArray([5,0,1,2,3,4]) == [4,5,0,1,2,3], "should be [4,5,0,1,2,3]"

if __name__ == "__main__":
    test_solutions()
    print("All tests pass!")