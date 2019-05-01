import numpy as np
import pandas as pd


def render(table, params):
    if not params['colnames']:
        return table

    for column in params['colnames']:
        series = table[column]
        fractions = series / series.sum()
        if fractions.isin([np.inf, -np.inf]).any():
            return (
                'The sum of "%s" is 0, so we cannot calculate percentages '
                'in it.'
            ) % column
        # We avoid duplicate columns by overwriting if there's a conflict
        table['percent_' + column] = fractions

    return {
        'dataframe': table,
        'column_formats': {f'percent_{c}': '{:,.1%}'
                           for c in params['colnames']},
    }


def _migrate_params_v0_to_v1(params):
    """v0: colnames is comma-separated str. v1: it's List[str]."""
    return {
        'colnames': [c for c in params['colnames'].split(',') if c],
    }


def migrate_params(params):
    if isinstance(params['colnames'], str):
        params = _migrate_params_v0_to_v1(params)
    return params
