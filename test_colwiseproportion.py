#!/usr/bin/env python3

import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from colwiseproportion import migrate_params, render


class MigrateParamsTest(unittest.TestCase):
    def test_v0_no_colnames(self):
        self.assertEqual(migrate_params({
            'colnames': '',
        }), {
            'colnames': [],
        })

    def test_v0(self):
        self.assertEqual(migrate_params({
            'colnames': 'A,B',
        }), {
            'colnames': ['A', 'B'],
        })

    def test_v1(self):
        self.assertEqual(migrate_params({
            'colnames': ['A', 'B'],
        }), {
            'colnames': ['A', 'B'],
        })


class RenderTest(unittest.TestCase):
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

    def test_divide_by_0(self):
        table = pd.DataFrame({'A': [-1, 1]})
        result = render(table, {'colnames': 'A'})
        self.assertEqual(
            result,
            'The sum of "A" is 0, so we cannot calculate percentages in it.'
        )

    def test_overwrite_colname(self):
        table = pd.DataFrame({'A': [1, 3], 'percent_A': ['x', 'y']})
        result = render(table, {'colnames': 'A'})
        expected = pd.DataFrame({
            'A': [1, 3],
            'percent_A': [0.25, 0.75],
        })
        assert_frame_equal(result, expected)
