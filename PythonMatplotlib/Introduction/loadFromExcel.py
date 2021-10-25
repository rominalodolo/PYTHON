import pandas as pd
from pandas import ExcelFile

df = pd.read_excel('PythonMatplotlib/Introduction/ExcelData.xlsx', sheet_name='Sheet1')

X = list(df['X'])
Y = list(df['Y'])
