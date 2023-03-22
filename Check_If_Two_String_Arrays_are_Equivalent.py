class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1) == ''.join(word2)

def test_solutions():
    solution = Solution()

    assert solution.arrayStringsAreEqual([""], [""]) == True, "should be []"
    assert solution.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) == True, "should be True"
    assert solution.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) == False, "should be False"
    assert solution.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) == True, "should be False"

if __name__ == "__main__":
    test_solutions()
    print("Everything passed!")
