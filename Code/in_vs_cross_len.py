import pandas as pd
base_hasoc = "data/HASOC/"
base_olid = "data/OLID-master/"
train_file_hasoc = base_hasoc + "HASOC_SOURCE_english_dataset_train_preprocessed.tsv"
test_file_hasoc = base_hasoc+  "HASOC_SOURCE_english_dataset_test_preprocessed.tsv"
train_file_olid = base_olid + "olid-training-v1.0.tsv"
train_file_olid_pp = base_olid +"olid-training-pp-labels.txt"
test_file_olid = base_olid + "olid-eval-preprocessed.tsv"
result_in_olid = "data/1_results_OLID/in-domain/in_domain_OLID_test_predicted.csv"
result_cross_olid = 'data/1_results_OLID/cross-domain/cross_domain_OLID_test_predicted.csv'
result_in_hasoc = "data/1_results_HASOC/in-domain/in_domain_HASOC_test_predicted.csv"
result_cross_hasoc = 'data/1_results_HASOC/cross-domain/cross_domain_HASOC_test_predicted.csv'

df_train_hasoc = pd.read_csv(train_file_hasoc, sep = "\t")
df_test_hasoc = pd.read_csv(test_file_hasoc, sep = "\t")
df_train_olid = pd.read_csv(train_file_olid, sep = "\t")
df_train_olid_pp = pd.read_csv(train_file_olid_pp, sep = "\t")
df_test_olid = pd.read_csv(test_file_olid, sep = "\t")
df_train_olid_pp = df_train_olid_pp[:5853]
df_result_in_olid = pd.read_csv(result_in_olid, sep = ",")
df_result_cross_olid = pd.read_csv(result_cross_olid, sep = ",")
df_result_in_hasoc = pd.read_csv(result_in_hasoc, sep = ",")
df_result_cross_hasoc = pd.read_csv(result_cross_hasoc, sep = ",")


def length(df):
    len_count = 0
    total_count = 0
    len_count_off = 0
    len_count_not =0
    len_count_not_instances = 0
    len_count_off_instances =0
    len_count_off_wrong = 0
    len_count_not_wrong = 0
    len_count_off_instances_wrong =0
    len_count_not_instances_wrong =0
    for index, row in df.iterrows():
        if row["labels"] == row["predicted"]:
            if row["labels"] == 1:
                len_count_off += len(row["text"])
                len_count_off_instances +=1
            else:
                len_count_not += len(row["text"])
                len_count_not_instances +=1
        if row["labels"] != row["predicted"]:
            if row["labels"] == 1:
                len_count_off_wrong += len(row["text"])
                len_count_off_instances_wrong +=1
            else:
                len_count_not_wrong += len(row["text"])
                len_count_not_instances_wrong +=1
        len_count += len(row["text"])
        total_count +=1

    print("average text length OFF correct", int(len_count_off)/int(len_count_off_instances))
    print("average text length NOT correct", int(len_count_not)/int(len_count_not_instances))
    print("average text length OFF wrong", int(len_count_off_wrong)/int(len_count_off_instances_wrong))
    print("average text length NOT wrong", int(len_count_not_wrong)/int(len_count_not_instances_wrong))

print(df_result_in_olid)
