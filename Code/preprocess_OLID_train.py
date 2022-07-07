import pandas as pd

inputfile_train = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/OLID-master/olid-training-v1.0.tsv"
output_file = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/OLID-master/olid-training-v1.0-preprocessed.tsv"
path_to_file = inputfile_train
df = pd.read_csv(path_to_file, sep="\t")
df = df.drop(columns="subtask_b")
df = df.drop(columns="subtask_c")
print(df)
df.loc[df["subtask_a"] == "OFF", "subtask_a"] = 1

df.loc[df["subtask_a"] == "NOT", "subtask_a"] = 0

df. rename(columns = {'tweet':'text', 'subtask_a':'labels'}, inplace = True)
print(df)
#df.to_csv(output_file, sep="\t", index=False)
