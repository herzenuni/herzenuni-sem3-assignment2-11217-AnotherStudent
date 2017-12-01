# python -m pytest test_sort.py -v

from sort import *
import pytest
import hypothesis.strategies as st
from hypothesis import given

@given(st.lists(st.integers()))
def test_bubble_sort(l):
	assert bubble_sort(l) == sorted(l)

@given(st.lists(st.integers()))
def test_quick_sort(l):
	assert quick_sort(l) == sorted(l)