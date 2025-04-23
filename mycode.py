import pandas as pd 
import os

data={
    'Name':['Alice','Charlie','Bob'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df=pd.DataFrame(data)


data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sampledata.csv')

df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")