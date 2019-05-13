# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:52:17 2016

@author: jennavergeynst
"""

import pandas as pd

def read_in_fathom_csv(path):
    """
    read in csv from fathom conversion (to timecorrected data with ms), keeping only detection information
    """
    fathom_df = pd.read_csv(path, skiprows=1, low_memory=False, encoding = "ISO-8859-1")
    det = fathom_df[fathom_df['RECORD TYPE'].isin(['DET_DESC', 'DET'])].reset_index(drop=True)
    det.rename(columns=det.iloc[0,], inplace=True)
    if len(det)>1: # only if detections occured
        det = det.reindex(det.index.drop(0)).dropna(how='all', axis=1).drop(columns='DET_DESC')
    else:
        det = [] # if not => return empty dataframe
    return det
