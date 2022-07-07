import sys
print(sys.path)
from simpletransformers.classification import ClassificationModel
import sklearn
import torch
import pandas as pd
import wandb

#paths to files
inputfile_train = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/OLID-master/olid-training-v1.0-preprocessed.tsv"
inputfile_eval = "path to file"

train_df = pd.read_csv(inputfile_train, sep="\t", header=0, names = ['ID', 'text', 'category'])
train_df = train_df[['text', 'category']]
#eval_df = pd.read_csv(inputfile_eval, sep="\t", header=0, names = ['ID', 'text', 'category'])
#eval_df = eval_df[['text', 'category']]
print(train_df)
