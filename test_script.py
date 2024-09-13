from script import __main__

class TestClass:

    def test_fail(self):
        assert __main__(5) == "*\n**\n***\n****\n*****\n****\n***\n**\n*\n"

    def test_pass(self):
        assert __main__(5) == "\n\n*\n*\n**\n*\n**\n\n\n"