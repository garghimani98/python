from openpyxl import load_workbook
import pandas as pd

import numpy as np

df1=pd.read_excel(r"C:\\Users\\User\\Documents\\File_name_with_extension")
df2=pd.read_excel(r"C:\\Users\\User\\Documents\\File_name_with_extension")

comparison_values = df1.values == df2.values
print (comparison_values)

rows,cols=np.where(comparison_values==False)

for item in zip(rows,cols):
    df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])
    
    df1.to_excel('./Excel_diff.xlsx',index=False,header=True)