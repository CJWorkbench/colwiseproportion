import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


def render(table, params):
    if not params['colnames']:
        # Do not process if no columns are selected
        return table

    columns = [c.strip() for c in params['colnames'].split(',')]

    valid_colnames = set(table.columns)

    missing_columns = []
    numeric_columns = []
    wrong_type_columns = []
    for column in columns:
        if column not in valid_colnames:
            missing_columns.append(column)
        elif not is_numeric_dtype(table[column]):
            wrong_type_columns.append(column)
        else:
            numeric_columns.append(column)

    focus_table = table.loc[:, numeric_columns]
    focus_sums = focus_table.sum()
    proportions_table = focus_table / focus_sums

    for column in proportions_table.columns:
        series = proportions_table[column]
        if series.isin([np.inf, -np.inf]).any():
            return (
                'The sum of "%s" is 0, so we cannot calculate percentages '
                'in it.'
            ) % column

    proportions_table.rename(columns=lambda c: 'percent_' + c, inplace=True)

    return pd.concat([table, proportions_table], axis=1)
