import re
import json

import numpy as np
import pandas as pd


usda_file = 'usda_plant2.csv'

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

    Example
    -------
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

    Example
    -------
    >>> d = {'a': 1, 'b': np.nan, 'c': 3}
    >>> d = remove_dict_nans(d)
    >>> sorted(d.keys())
    ['a', 'c']
    """
    return {k : d[k] for k in d if pd.notnull(d[k])}

def nested_dict(dicts):
    """Convert a list of dictionaries into a nested dictionary
    with the scientific name as keys

    Parameters
    ----------
    dicts : list

    Returns
    -------
    dict

    Notes
    -----
    Using scientific name instead of common name because of
    duplicate common names

    Example
    -------
    >>> x = [{'scientific_name' : 'a', 'something' : 2},
    ...      {'scientific_name' : 'b', 'something' : 3}]
    >>> d = nested_dict(x)
    >>> sorted(d.keys())
    ['a', 'b']
    """
    assert isinstance(dicts, list)
    return {d['scientific_name'].lower() : d for d in dicts}

def usda_dicts():
    """Convert the USDA data to a nested dictionary"""
    df = pd.read_csv(usda_file)
    cols_orig = df.columns
    df.columns = [normalize(c) for c in cols_orig]
    usda = df.to_dict(orient='record')
    usda = [remove_dict_nans(item) for item in usda]
    assert df.shape[0] == len(usda)
    return nested_dict(usda)


if __name__ == '__main__':
    from sys import argv
    args = len(argv) > 1
    if args:
        if argv[1] == 'create':
            j = usda_dicts()
            with open('usda.json', 'w') as f:
                json.dump(j, f, indent=4)
    else:
        import doctest
        doctest.testmod()
