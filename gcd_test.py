# python -m pytest gcd_test.py -v

from gcd import *
import pytest

@pytest.mark.parametrize("a,b,expected", [
  (18,45,9),
  (10,15,5),
  (12,20,4),
  (18,45,9),
  (48,36,12),
  (0,0,0)])
def test_gcd(a,b,expected):
    assert(gcd(a,b) == expected)

import hypothesis.strategies as st
from hypothesis import given

@given(st.integers(), st.integers())
def test_hyp_gcd(x, y):
    if(gcd(x,y) != 0):
        assert((x % gcd(x,y) == 0) and (y % gcd(x,y) == 0))