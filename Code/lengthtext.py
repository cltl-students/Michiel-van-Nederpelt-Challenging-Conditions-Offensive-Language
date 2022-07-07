import pandas as pd
base_hasoc = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/HASOC/"
base_olid = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/OLID-master/"
train_file_hasoc = base_hasoc + "HASOC_SOURCE_english_dataset_train_preprocessed.tsv"
test_file_hasoc = base_hasoc+  "HASOC_SOURCE_english_dataset_test_preprocessed.tsv"
train_file_olid = base_olid + "olid-training-v1.0.tsv"
train_file_olid_pp = base_olid +"olid-training-pp-labels.txt"
test_file_olid = base_olid + "olid-eval-preprocessed.tsv"
result_in_olid = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/1_results_OLID/in-domain/in_domain_OLID_test_predicted.tsv"
result_cross_olid = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/1_results_OLID/cross-domain/cross_domain_OLID_test_predicted.csv"
result_in_hasoc = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/1_results_HASOC/in-domain/in_domain_HASOC_test_predicted.csv"
result_cross_hasoc = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/1_results_HASOC/cross-domain/cross_domain_HASOC_test_predicted.csv"
inputfile_off = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/wordlists/all_caps.tsv"

df_off = pd.read_csv(inputfile_off, sep="\t")
df_train_hasoc = pd.read_csv(train_file_hasoc, sep = "\t")
df_test_hasoc = pd.read_csv(test_file_hasoc, sep = "\t")
df_train_olid = pd.read_csv(train_file_olid, sep = "\t")
df_train_olid_pp = pd.read_csv(train_file_olid_pp, sep = "\t")
df_test_olid = pd.read_csv(test_file_olid, sep = "\t")
df_train_olid_pp = df_train_olid_pp[:5853]


df_result_in_olid = pd.read_csv(result_in_olid, sep = "\t",  index_col=[0])
df_result_cross_olid = pd.read_csv(result_cross_olid, sep = ",")
df_result_in_olid["cross-predicted"] = df_result_cross_olid ["predicted"]

df_result_in_hasoc =  pd.read_csv(result_in_hasoc, sep = ",", index_col=[0])

df_result_cross_hasoc =  pd.read_csv(result_cross_hasoc, sep = ",", index_col=[0])
df_result_in_hasoc["cross-predicted"] = df_result_cross_hasoc["predicted"]

def length(df):
    #len_count_correct = 0
    #len_count_wrong = 0
    count_correct_total = 0
    count_wrong_total = 0
    long_correct_count  = 0
    long_instance_total = 0
    count_correct_long =0
    count_wrong_long =0
    for index, row in df.iterrows():
        if row["predicted"] == row["labels"]:
            count_correct_total +=1
        if row["predicted"] != row["labels"]:
            count_wrong_total +=1
        if len(row["text"]) > 240:
            long_instance_total +=1
            if row["predicted"] == row["labels"]:
                #len_count_correct += len(row["text"])
                count_correct_long +=1
            if row["predicted"] != row["labels"]:
                #len_count_wrong += len(row["text"])
                count_wrong_long +=1
    print("total long instances in dataset: ", long_instance_total)
    print("count_correct_total" , count_correct_total)
    print("correct count large instances:")
    print(count_correct_long)
    print("percentage of correct long predictions over total correct predictions: " , int(count_correct_long)/int(count_correct_total))
    #print(long_correct_count)
    #print("percentage correct predictions large instances: ", int(long_correct_count)/int(total_count_correct))
    print("count_wrong_total" , count_wrong_total)
    print("wrong count large instances: ")
    print(count_wrong_long)
    print("percentage of wrong long predictions over total wrong predictions: ", int(count_wrong_long)/int(count_wrong_total))
    #print(long_wrong_count)
    #print("average text length incorrect predictions long instances: ", int(long_wrong_count)/int(total_count_wrong))

def no_offensive_words(df, df_off):
    #used to count instances
    count = 0
    count_offensive_instances  =0
    count_offensive_instances_correct  = 0
    count_words_correct_offensive = 0
    count_offensive_instances_wrong =0
    count_words_wrong_offensive = 0
    count_not_offensive_instances = 0
    count_not_instances_correct = 0
    count_words_correct_not = 0
    count_words_wrong_not = 0
    count_not_instances_wrong = 0

    #find offensive word per text instance
    for index, row_df in df.iterrows():
        if row_df["labels"] == 1:
            count_offensive_instances +=1
            if row_df["labels"] == row_df["predicted"]:
                count_offensive_instances_correct +=1
                for index, row in df_off.iterrows():
                    if row["original"] in row_df["text"]:
                        row_df["text"] = row_df["text"].replace(row["original"], row["new"])
                        #count
                        count_words_correct_offensive += 1
            if row_df["labels"] != row_df["predicted"]:
                count_offensive_instances_wrong +=1
                for index, row in df_off.iterrows():
                    if row["original"] in row_df["text"]:
                        row_df["text"] = row_df["text"].replace(row["original"], row["new"])
                        #count
                        count_words_wrong_offensive += 1
        if row_df["labels"] == 0:
            count_not_offensive_instances +=1
            if row_df["labels"] == row_df["predicted"]:
                count_not_instances_correct +=1
                for index, row in df_off.iterrows():
                    if row["original"] in row_df["text"]:
                        row_df["text"] = row_df["text"].replace(row["original"], row["new"])
                        #count
                        count_words_correct_not += 1
            if row_df["labels"] != row_df["predicted"]:
                count_not_instances_wrong +=1
                for index, row in df_off.iterrows():
                    if row["original"] in row_df["text"]:
                        row_df["text"] = row_df["text"].replace(row["original"], row["new"])
                        #count
                        count_words_wrong_not += 1

    average_words_offensive_instance_correct = int(count_words_correct_offensive)/int(count_offensive_instances_correct)
    average_words_offensive_instance_wrong = int(count_words_wrong_offensive)/int(count_offensive_instances_wrong)
    average_words_not_offensive_instance_correct = int(count_words_correct_not)/int(count_not_instances_correct)
    average_words_not_offensive_instance_wrong = int(count_words_wrong_not)/int(count_not_instances_wrong)

    print("number of offensive words in correct offensive instance:", average_words_offensive_instance_correct)
    print("number of offensive words in wrong offensive instance:", average_words_offensive_instance_wrong)
    print("number of offensive words in correct not offensive instance:", average_words_not_offensive_instance_correct)
    print("number of offensive words in wrong not offensive instances:", average_words_not_offensive_instance_wrong)


def special_characters(df):
    count_correct = 0
    count_incorrect =0
    no_special_wrong = 0
    no_special_correct =0
    for index, row in df.iterrows():
        if row["labels"] == row["predicted"]:
            count_correct +=1
            no_special_correct += sum(not (q.isalpha() or q==" " or q == ',' or q == ".") for q in row["text"].lower())

        if row["labels"] != row["predicted"]:
            count_incorrect +=1
            no_special_wrong += sum(not (q.isalpha() or q==" " or q == ',' or q == ".") for q in row["text"].lower())
    print("average number of special tokens correct predictions:", no_special_correct/count_correct)
    print("average number of special tokens wrong predictions:", no_special_wrong/count_incorrect)




special_characters(df_result_in_hasoc)
#length(df_result_in_olid)
#no_offensive_words(df_result_in_olid, df_off)
