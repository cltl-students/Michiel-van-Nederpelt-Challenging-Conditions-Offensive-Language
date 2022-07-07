import pandas as pd



result_cross_olid = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/1_results_OLID/cross-domain/cross_domain_OLID_test_predicted.csv"

infile = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/1_results_OLID/in-domain/offensive_predicted_political.txt"


df_olid_cross = pd.read_csv(result_cross_olid,  index_col=[0])
df_olid_in = pd.read_csv(infile, sep = "\t", index_col=[0])
offensive_list = []

def offensive_instances(df):
    count_correct_predicted = 0
    count_correct_political = 0
    count_correct_non_political = 0
    count_wrong_predicted = 0
    count_wrong_political = 0
    count_wrong_non_political =0
    count_political = 0
    count_total = 0
    #find offensive word per text instance
    for index, row in df.iterrows():
        count_total +=1
        if row["predicted"] == row["cross-predicted"]:
            if row["political"] ==1:
                count_correct_political +=1
            if row["political"] == 0:
                count_correct_non_political +=1
        if row["labels"] != row["cross-predicted"]:
            count_wrong_predicted +=1
            if row["political"] ==1:
                count_wrong_political +=1
            if row["political"] == 0:
                count_wrong_non_political +=1
    print("count_correct_predicted ",  count_correct_predicted )
    print("count_correct_political", count_correct_political)
    print("count_correct_non_political", count_correct_non_political)
    print("\n")
    print("count_wrong_predicted", count_wrong_predicted)
    print("count_wrong_political",  count_wrong_political)
    print("count_wrong_non_political",  count_wrong_non_political)
    print("total political :", count_political)
    print(count_total)

def difference_in_vs_cross (df):
    easy_list =[]
    hard_list = []
    in_correct_list = []
    cross_correct_list = []

    for index, row in df.iterrows():
        if row["predicted"] == row["cross-predicted"]:
            if row["labels"] == row["predicted"]:
                easy_list.append(row)
            if row["labels"] != row["predicted"]:
                hard_list.append(row)
        if row["predicted"] != row["cross-predicted"]:
            if row["predicted"] == row["labels"]:
                in_correct_list.append(row)
            if row["cross-predicted"] == row["labels"]:
                cross_correct_list.append(row)
    df_easy = pd.DataFrame(easy_list)
    df_hard = pd.DataFrame(hard_list)
    df_in_correct = pd.DataFrame(in_correct_list)
    df_cross_correct = pd.DataFrame(cross_correct_list)
    print(df_easy)


df_olid_in["cross-predicted"] = df_olid_cross["predicted"]
offensive_instances(df_olid_in)
difference_in_vs_cross (df_olid_in)
