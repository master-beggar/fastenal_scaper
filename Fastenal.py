import pandas as pd
import os

os.chdir(r'C:\Users\wnaimi\Desktop\Fastenal Fasteners')

txt_file = "Fasteners.txt"

part_numbers = []
with open(txt_file) as file:
    for line in file:
        line = line.strip()
        line = line.split('\t')
        if len(line) > 1:
            line = line[0]
            part_numbers.append(line)

with open('new_fasteners.txt', 'w') as file:
    for part in part_numbers:
        search = "https://www.fastenal.com/products/details/" + part
        table = pd.read_html(search, attrs = {'class':'table product__attribute--info'})
        prod = table[0].T
        prod.columns = prod.iloc[0]
        prod = prod.reindex(prod.index.drop(0))

        if 'Finish' in prod:
            prod_finish = ''.join(prod.Finish.tolist())
        if 'Type' in prod:
            prod_type = ''.join(prod.Type.tolist())
        if 'Material' in prod:
            prod_material = ''.join(prod.Material.tolist())
        if 'Length' in prod:
            prod_length = ''.join(prod.Length.tolist())
        if 'Diameter - Thread Size' in prod:
            prod_diam_thread = ''.join(prod['Diameter - Thread Size'].tolist())
        if 'Diameter-Thread Size' in prod:
            prod_diam_thread = ''.join(prod['Diameter-Thread Size'].tolist())
        
    ##        file.write('{} - {} - {} - {} \n'.format(part, prod_finish, prod_material, prod_type))
        if 'Diameter - Thread Size' in prod and 'M' in prod['Diameter - Thread Size'][1]:
            file.write('{}|{}|{}|{}|{}|{}\n'.format(part, prod_diam_thread, prod_length, prod_type,prod_material,prod_finish))
        if 'Diameter-Thread Size' in prod and 'M' in prod['Diameter-Thread Size'][1]:
            file.write('{}|{}|{}|{}|{}|{}\n'.format(part, prod_diam_thread, prod_length, prod_type,prod_material,prod_finish))

