import pandas as pd

train_file_path ='train.tsv' 
train_data = pd.read_table(train_file_path,header=None)
# print (train_data)

description_file_path ='description.csv'
description_data = pd.read_csv(description_file_path)
# print (description_data)

merge_table = pd.merge(train_data, description_data, left_on=3, right_on='liczba', how='left')
merge_table = merge_table.drop(columns='liczba')
merge_table.to_csv('out2.csv', index=False, header=None)

check = pd.read_csv('out2.csv')
print(check)
