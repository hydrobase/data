import os
import re
import json
import subprocess
from collections import defaultdict

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

def data(f):
    """Load and normalize `usda_file`

    Parameters
    ----------
    f : str
        filename

    Returns
    -------
    df : pd.DataFrame

    Example
    --------
    >>> rows = int(subprocess.check_output(['wc', '-l', usda_file]).split()[0])
    >>> df = data(usda_file)
    >>> rows == df.shape[0]
    True
    """
    df = pd.read_csv(f)
    cols_orig = df.columns
    df.columns = [normalize(c) for c in cols_orig]
    return df

def usda_dicts(df):
    """Convert `df` to a nested dictionary"""
    df = df.copy()
    usda = df.to_dict(orient='record')
    usda = [remove_dict_nans(item) for item in usda]
    assert df.shape[0] == len(usda)
    return nested_dict(usda)

def mapping(df):
    df = df.copy()
    names_mapping = defaultdict(list)
    for i in df.index:
        names_mapping[df.common_name[i]].append(df.scientific_name[i])
    return dict(names_mapping)

def to_json(d, filename):
    """Dictionary to JSON

    Parameters
    ----------
    d : dict
    filename : str

    Returns
    -------
    None

    Example
    -------
    >>> d = {'one' : 1}
    >>> filename = 'test.json'
    >>> to_json(d, filename)
    >>> with open(filename, 'r') as f:
    ...     d_ = json.load(f)
    >>> os.remove(filename)
    >>> d == d_
    True
    """
    assert isinstance(d, dict)
    assert isinstance(filename, str)
    with open(filename, 'w') as f:
        json.dump(d, f, indent=4)

def main():
    df = data(usda_file)
    usda_json = usda_dicts(df)
    to_json(usda_json, 'usda.json')
    names_map = mapping(df)
    to_json(names_map, 'mapping.json')


if __name__ == '__main__':
    from sys import argv
    args = len(argv) > 1
    if args:
        if argv[1] == 'create':
            main()
        else:
            print("'{}' is not a valid argument".format(argv[1]))
    else:
        import doctest
        doctest.testmod()
