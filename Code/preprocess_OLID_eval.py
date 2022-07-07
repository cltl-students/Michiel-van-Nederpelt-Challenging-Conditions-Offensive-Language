import pandas as pd

inputfile_text = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/OLID-master/testset-levela.tsv"
inputfile_labels = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/OLID-master/labels-levela.csv"
output_file = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/OLID-master/olid-eval-preprocessed-try.tsv"


df_text = pd.read_csv(inputfile_text, sep="\t")
df_labels = pd.read_csv(inputfile_labels, sep=",", names=['ID', 'label'])


df_labels.loc[df_labels["label"] == "OFF", "label"] = 1

df_labels.loc[df_labels["label"] == "NOT", "label"] = 0


df_together = df_text.join(df_labels)
df_together = df_together.drop(columns="ID")
df_together. rename(columns = {'tweet':'text'}, inplace = True)
print(df_together)
df_together = df_together[0:25]
print(df_together)
df_together.to_csv(output_file, sep="\t", index=False)
