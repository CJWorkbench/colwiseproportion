#!/usr/bin/env python3

import datetime
import unittest
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
from colwiseproportion import render


class ColwiseProportionTest(unittest.TestCase):
    def test_no_params(self):
        table = pd.DataFrame({'A': [1, 2], 'B': [2, 3]})
        expected = table.copy()
        result = render(table, {'colnames': ''})
        assert_frame_equal(result, expected)

    def test_basic(self):
        table = pd.DataFrame({'A': [1, 2], 'B': [2, 3], 'C': [3, 4]})
        result = render(table, {'colnames': 'A,B'})
        expected = pd.DataFrame({
            'A': [1, 2],
            'B': [2, 3],
            'C': [3, 4],
            'percent_A': [1/3, 2/3],
            'percent_B': [0.4, 0.6],
        })
        assert_frame_equal(result, expected)

    def test_ignore_non_numbers(self):
        now = datetime.datetime.now()
        table = pd.DataFrame({
            'A': ['1', '2'],
            'B': [2, 3],
            'C': [now, np.NaN],
        })
        result = render(table, {'colnames': 'A,B,C'})
        expected = pd.DataFrame({
            'A': ['1', '2'],
            'B': [2, 3],
            'C': [now, np.NaN],
            'percent_B': [0.4, 0.6],
        })
        assert_frame_equal(result, expected)
