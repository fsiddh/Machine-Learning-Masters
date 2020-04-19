import pandas as pd
import numpy as np
"""
Problem Statement

It happens all the time: someone gives you data containing malformed strings,
Python, lists and missing data.
How do you tidy it up so you can get on with the analysis?

Take this monstrosity as the DataFrame to use in the following puzzles:
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
"""

"""
1. Some values in the the FlightNumber column are missing. These numbers are
meant to increase by 10 with each row so 10055 and 10075 need to be put in
place. Fill in these missing numbers and make the column an integer column
(instead of a float column).
"""

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
                               'londON_StockhOlm', 'Budapest_PaRis',
                               'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13],
                                    [67, 32]], 'Airline': ['KLM(!)',
                                                           '<Air France> (12)',
                                                           '(British Airways)',
                                                           '12. Air France',
                                                           '"Swiss Air"']})

df.iloc[1, 1] = 10055
df.iloc[3, 1] = 10075
df_new = df['FlightNumber'].astype('int64')
df['FlightNumber'] = df_new

print(df)

"""
2. The From_To column would be better as two separate columns! Split each
string on the underscore delimiter _ to give a new temporary DataFrame with
the correct values. Assign the correct column names to this temporary
DataFrame.
"""

df['From_To'][0].split()

print(df.head())
