
import pandas as pd
import os

# all_csv = [file_name for file_name in os.listdir(os.getcwd()) if '.csv' in file_name]

all_csv = [file_name for file_name in "./data/*.csv"]

li = []
col_to_del = ['open', 'high', 'low', 'AdjClose', 'dividend', 'split']

# would like to label columns with file name
for filename in all_csv:
    df = pd.read_csv(filename, skiprows=1)
    df.columns = ['date','open','high','low','close','AdjClose','vol','dividend','split']
    df.drop(col_to_del, inplace=True, axis=1)
    df['date'] = df['date'].astype('datetime64[ns]')
    df.set_index('date', inplace=True)
    li.append(df)

frame = pd.concat(li, axis=1)
frame.to_csv('all_etfs.csv')




