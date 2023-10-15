import unittest
from gradescope_utils.autograder_utils.decorators import weight
from app import *

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @weight(1)
    def test_index_link(self):
        response = self.client.get("/")
        assert b"<a" in response.data
        assert b'href="/game"' in response.data or b"href='/game'" in response.data
    
    @weight(2)
    def test_numbers_appear(self):
        response = self.client.get("/game")
        assert b"1" in response.data
        assert b"10" in response.data
        assert b"45" in response.data
        assert b"82" in response.data
    
    @weight(1)
    def test_low(self):
        game = self.client.get("/game")
        guess = self.client.get("/guess/1")
        assert b"low" in guess.data or b"Low" in guess.data
    
    @weight(1)
    def test_high(self):
        game = self.client.get("/game")
        guess = self.client.get("/guess/99")
        assert b"high" in guess.data or b"High" in guess.data

if __name__ == "__main__":
    unittest.main()
