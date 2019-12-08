#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 00:31:30 2019

@author: Dun
"""

def keyvalues(text, sep1, sep2):
    result = {}
    ls = map(lambda x: map(lambda x: x.strip(), x), 
             map(lambda x: x.split(sep2), text.split(sep1)))
    result.update(list(map(list, ls)))
    return result

s = 'a = 200, b = 300'
keyvalues(s, ',', '=')

df = pd.DataFrame({'user_id': [1000, 1000, 1000, 2000],
                   'category': ['EL', 'FMCG', 'FMCG', 'GM'],
                   'gmv': [100, 200, 500, 2000],
                   'units': [2, 5, 20, 1]})
    
def count(x):
    return len(x)
    
p_df = df.pivot_table(index = 'user_id',
                      columns = 'category',
                      values = ['gmv', 'units'],
                      aggfunc = [np.sum, count],
                      fill_value = 0)

p_df.columns = p_df.columns.map('_'.join)

