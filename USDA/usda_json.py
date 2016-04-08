import re

import numpy as np
import pandas as pd


def normalize(s):
    """Removes text within angled brackets
    Removes commas, parens, and degree symbols
    Replaces spaces and forward slashes with underscores
    To lowercases

    Parameters
    ----------
    s : str

    Returns
    -------
    s : str

    Examples
    --------
    >>> s = '°UC (Berkeley), I/School°<South Hall>'
    >>> normalize(s)
    'uc_berkeley_i_school'
    """
    s = re.sub('\<.*?\>', '', s)
    return re.sub('[\s\/]+', '_', re.sub('[,()°]+', '', s)).lower()

def remove_dict_nans(d):
    """Remove items with missing value values

    Parameters
    ----------
    d : dict

    Returns
    -------
    d : dict

    Examples
    --------
    >>> d = {'a': 1, 'b': np.nan, 'c': 3}
    >>> d = remove_dict_nans(d)
    >>> sorted(d.keys())
    ['a', 'c']
    """
    return {k : d[k] for k in d if pd.notnull(d[k])}

def usda_json():
    """Convert the USDA data to a list of dictionaries

    Returns
    -------
    usda_json : list
        a list of dicts, one for each record in the data file
    """
    df = pd.read_csv('usda_plant2.csv')
    cols_orig = df.columns
    df.columns = [normalize(c) for c in cols_orig]
    usda_json = df.to_dict(orient='record')
    usda_json = [remove_dict_nans(item) for item in usda_json]
    assert df.shape[0] == len(usda_json)
    return usda_json


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    usda_json()
