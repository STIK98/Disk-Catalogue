import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

load = pd.read_csv("Dataset_full.txt" , sep='\t', engine='python')
print(load)

#print(load.columns)
#print(load.iloc[1])

#for index, row in load.iterrows():
    #print(index,row['OBJECT'])

#print(load.loc[load['Type'] == "OBJECT"])

#print(load.loc[load['TPL ID'] == "SPHERE_irdis_dpi_obs"])