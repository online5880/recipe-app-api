"""
샘플 테스트
"""
from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """
    계산 모듈 테스트
    """
    def test_add_numbers(self):
        """
        덧셈 계산 테스트
        """
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)
        
    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 15)
        
        self.assertEqual(res, 5)