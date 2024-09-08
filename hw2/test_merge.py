from hw2_debugging import mergeSort

class TestClass:
    def test_one(self):
        res = mergeSort([0, -1, 1])
        assert res == [-1, 0, 1]

    def test_two(self):
        res = mergeSort([17, 2, 11, 12, 10, 16, 4, 14, 13, 6, 18, 8, 4, 10, 3, 3, 5, 20, 6, 20])
        assert res == [2, 3, 3, 4, 4, 5, 6, 6, 8, 10, 10, 11, 12, 13, 14, 16, 17, 18, 20, 20]

    def test_three(self):
        res = mergeSort([100])
        assert res == [100]