import pandas as pd

print("hello world")

from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt


# inputfiles
inputfile_train = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/OLID-master/labels-levela.csv"
inputfile_dev = 'data/SEM-2012-SharedTask-CD-SCO-dev-simple.v2.features.conll'

# outputfiles

path_to_file = inputfile_train
df = pd.read_csv(path_to_file, sep=",")
df = df.drop(columns="subtask_b")
df = df.drop(columns="subtask_c")
print(df)
for col in df:
    print(df[col]. value_counts())
print(df["tweet"].apply(len).mean())
print(df.fillna('').astype(str).apply(lambda x:x.str.len()).mean())
