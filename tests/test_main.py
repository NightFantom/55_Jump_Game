from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_can_jump_1(self):
        jumps = [2, 3, 1, 1, 4]
        result = Solution().canJump(jumps)
        self.assertTrue(result)

    def test_can_jump_2(self):
        jumps = [4, 0, 1, 0, 2]
        result = Solution().canJump(jumps)
        self.assertTrue(result)

    def test_can_jump_3(self):
        jumps = [3, 5, 2, 0, 0, 0, 2]
        result = Solution().canJump(jumps)
        self.assertTrue(result)

    def test_can_jump_4(self):
        jumps = [4, 0, 5, 0, 1, 0, 0, 4]
        result = Solution().canJump(jumps)
        self.assertTrue(result)

    def test_can_jump_5(self):
        jumps = [10, 0, 3]
        result = Solution().canJump(jumps)
        self.assertTrue(result)

    def test_can_jump_6(self):
        jumps = [2, 0, 0]
        result = Solution().canJump(jumps)
        self.assertTrue(result)

    def test_can_jump_7(self):
        jumps = [10, 1, 1, 1, 1, 1, 1, 0, 1]
        result = Solution().canJump(jumps)
        self.assertTrue(result)

    def test_can_not_jump_1(self):
        jumps = [3, 2, 1, 0, 4]
        result = Solution().canJump(jumps)
        self.assertFalse(result)

    def test_can_not_jump_2(self):
        jumps = [3, 4, 2, 0, 0, 0, 2]
        result = Solution().canJump(jumps)
        self.assertFalse(result)

    def test_can_not_jump_3(self):
        jumps = [0, 1]
        result = Solution().canJump(jumps)
        self.assertFalse(result)

    def test_can_not_jump_4(self):
        jumps = [1,1,0,1]
        result = Solution().canJump(jumps)
        self.assertFalse(result)



