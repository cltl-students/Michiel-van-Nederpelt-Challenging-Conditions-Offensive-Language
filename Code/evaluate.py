import pandas as pd

inputfile_in_domain = "data/results_OLID_test/in-domain/OLID_train_OLID__test_predicted.csv"
inputfile_hasoc_cross_domain = "data/results_HASOC_test/in-domain/OLID_train_HASOC__test_predicted.csv"

#load predictions in dataframes
df_in_domain = pd.read_csv(inputfile_in_domain, sep=",", index_col=[0])
df_hs_cross = pd.read_csv(inputfile_hasoc_cross_domain , sep=",", index_col=[0])
#empty data frames
df_in_domain_wrong_pred = pd.DataFrame(columns = ["text", "labels", "predicted"])
df_hs_cross_wrong_pred = pd.DataFrame(columns = ["text", "labels", "predicted"])
print(df_in_domain)

count = 0
a_list = []
for index, row in df_in_domain.iterrows():
        if row["labels"] != row["predicted"]:
            count += 1
            df_in_domain_wrong_pred=df_in_domain_wrong_pred.append(row)
print(count)
print(df_in_domain_wrong_pred)


print(df_hs_cross)

count = 0
a_list = []
for index, row in df_hs_cross.iterrows():
        if row["labels"] != row["predicted"]:
            count += 1
            df_hs_cross_wrong_pred=df_hs_cross_wrong_pred.append(row)
print(count)
print(df_hs_cross_wrong_pred)
