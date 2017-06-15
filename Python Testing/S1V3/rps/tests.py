import unittest

import moves

class MoveTests(unittest.TestCase):
    def test_five_plus_five(self):
        assert 5 + 5 ==10

    
    def test_one_plus_one(self):
        assert not 1 + 1 == 3


    def test_equal(self):
        rock1 = moves.Rock()
        rock2 = moves.Rock()

        self.assertEqual(rock1, rock2)
    
    def test_not_equal(self):
        rock = moves.Rock()
        paper = moves.Paper()

        self.assertNotEqual(rock, paper)
        
if __name__ == '__main__':
    unittest.main()


