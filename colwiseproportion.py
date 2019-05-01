import numpy as np
import pandas as pd


def render(table, params):
    columns = [c for c in params['colnames'].split(',') if c]

    for column in columns:
        series = table[column]
        fractions = series / series.sum()
        if fractions.isin([np.inf, -np.inf]).any():
            return (
                'The sum of "%s" is 0, so we cannot calculate percentages '
                'in it.'
            ) % column
        # We avoid duplicate columns by overwriting if there's a conflict
        table['percent_' + column] = fractions

    return table
