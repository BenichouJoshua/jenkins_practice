import factorial
import pytest

class TestFactorial:
    def test_positives(self):
        assert 1 == factorial.Factorial(1)
        assert 2 == factorial.Factorial(2)
        assert 6 == factorial.Factorial(3)
        assert 24 == factorial.Factorial(4)

    def test_negatives(self):
        with pytest.raises(RuntimeError):
            factorial.Factorial(-1)     
