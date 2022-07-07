#from google.colab import files
#uploaded_files = files.upload()

from simpletransformers.classification import ClassificationModel
import sklearn
import torch
import pandas as pd
import wandb
wandb_project = "SimpleTransformers-OLID-in-domain(1)"


#paths to files
inputfile_train = "olid-training-v1.0-preprocessed.tsv"
inputfile_eval = "olid-eval-preprocessed.tsv"

#load the data into pandas dataframe
train_df = pd.read_csv(inputfile_train, sep="\t", header=0, names = ['ID', 'text', 'labels'])
train_df = train_df[['text', 'labels']]
eval_df = pd.read_csv(inputfile_eval, sep="\t", header=0, names = ['ID', 'text', 'labels'])
eval_df = eval_df[['text', 'labels']]
train_df.columns = ['text','labels']
eval_df.columns = ['text','labels']


model_args = {
    "num_train_epochs": 2,
    "learning_rate": 1e-4,
    "output_dir" : 'outputs/OLID/',
    'overwrite_output_dir':            True, # overwrite the output directory
    'reprocess_input_data':           False, # reprocess the input data
    'gradient_accumulation_steps':        1, # steps before applying gradients
    'evaluate_during_training':        True, # run evaluation during training
    'evaluate_during_training_steps':    40, # steps in training before eval
    'save_eval_checkpoints':          False, # save evaluation checkpoints
    'eval_batch_size':                   16, # evaluation batch size
}


#this is used for WandB visualization
model_args.update(
    {
        "logging_steps":                      1, # number of steps before logging
        "wandb_project":          wandb_project, # wandb project name
        "wandb_kwargs": {"job_type": "training"} # additional args for wandb init
    }
)
#check if cuda available, otherwise skip
cuda_available = torch.cuda.is_available()
#define model
model = ClassificationModel('bert', 'bert-base-cased', args=model_args, use_cuda=cuda_available)
# Train the model
model.train_model(train_df, eval_df=eval_df)
#evaluate model
model.eval_model(eval_df, acc=sklearn.metrics.accuracy_score)
#original
#model.train_model(train_df, acc=sklearn.metrics.accuracy_score)
