import pandas as pd

table = pd.read_excel(r'./excel_files/Angstrom Fasteners 1.xlsx', header=0)

table.columns = pd.DataFrame(['Part Number', 'Description'])

print(table['Part Number'])
