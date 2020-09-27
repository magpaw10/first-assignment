import pandas as pd

train_file_path ='train.tsv' 
train_data = pd.read_table(train_file_path,sep='\t',header=None)
print (train_data)

average_price = round(train_data[[0]].mean())
average_price.to_csv('out0.csv',header=None,index=False)

train_data[5] = round(train_data[0]/train_data[2],2)
print (train_data)

average_m2 = train_data[5].mean()

print (average_m2)

train_data_2 = train_data[(train_data[1] >= 3) & (train_data[5] < average_m2)]
print (train_data_2)

train_data_2.to_csv('out1.csv', columns=[1,0,5],header=None,index=False)


