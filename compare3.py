from openpyxl import load_workbook
import pandas as pd
import openpyxl as xl
import numpy as np
from pathlib import Path

#define parameters
#path to files
path_old=Path(r"")
path_new=Path(r"")


#list of key column(s)
key=['Clrcd']

#sheets to read in
sheet='Sheet1'

# Read in the two excel files and fill NA
old = pd.read_excel(path_old,sheet_name='Sheet1',index_col=0)
new = pd.read_excel(path_new,sheet_name='Sheet1',index_col=0)

#data_top = old.head()

#set index
old=old.set_index(key)
new=new.set_index(key)

#to find number of columns and rows
m_c1=len(old. columns)
index = old.index
m_r1= len(index)

#identify dropped rows and added (new) rows
dropped_rows = set(old.index) - set(new.index)
dropped = old.loc[dropped_rows]

#create a name for the output excel file
fname =  '{} vs {}.xlsx'.format(path_old.stem, path_new.stem)

#write dataframe to excel
writer=pd.ExcelWriter(fname, engine='xlsxwriter')
dropped.to_excel(writer, sheet_name='dropped', index=True)

#get xlswriter objects
workbook = writer.book
worksheet = writer.sheets['dropped']
worksheet.hide_gridlines(2)
worksheet.set_default_row(15)
print(worksheet)

#get number of rows of the df diff
row_count_str=str(len(dropped.index)+1)
print(row_count_str)
#define and apply formats
highligt_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color':'#B1B3B3'})
worksheet.conditional_format('A1:ZZ'+row_count_str, {'type':'text', 'criteria':'containing', 'value':'--->',
                            'format':highligt_fmt})


writer.save()


