import pandas as pd

inputfile_train = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/HASOC/hasoc2019_en_test-2919.tsv"
output_file = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/HASOC/HASOC_SOURCE_english_dataset_test_preprocessed.tsv"
path_to_file = inputfile_train
df = pd.read_csv(path_to_file, sep="\t")
df = df.drop(columns="task_2")
df = df.drop(columns="task_3")
print(df)
df.loc[df["task_1"] == "HOF", "task_1"] = 1

df.loc[df["task_1"] == "NOT", "task_1"] = 0

df. rename(columns = {'task_1':'labels'}, inplace = True)
print(df)
df.to_csv(output_file, sep="\t", index=False)
