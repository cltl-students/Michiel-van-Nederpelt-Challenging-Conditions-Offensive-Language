import pandas as pd



base_olid = "data/1_results_OLID/in_vs_cross/"
base_hasoc = "data/1_results_HASOC/in_vs_cross/"

easy_instances_input = base_olid + "correct_easy_predicitions.csv"
easy_offensive_instances_input = base_olid +"correct_offensive_easy_predicitions.csv"
easy_not_offensive_instances_input = base_olid +"correct_notoffensive_easy_predicitions.csv"

hard_instances_input = base_olid + "wrong_hard_predicitions.csv"
hard_offensive_instances_input = base_olid +"wrong_offensive_hard_predicitions.csv"
hard_not_offensive_instances_input = base_olid +"wrong_notoffensive_hard_predicitions.csv"

cross_correct_in_wrong_input = base_olid +"cross_correct_in_wrong.csv"
cross_correct_in_wrong_offensive_input = base_olid +  "cross_correct_in_wrong_offensive.csv"
cross_correct_in_wrong_not_offensive_input = base_olid + "cross_correct_in_wrong_not_offensive.csv"
in_correct_cross_wrong_input = base_olid + "in_correct_cross_wrong.csv"
in_correct_cross_wrong_offensive_input = base_olid +  "in_correct_cross_wrong_offensive.csv"
in_correct_cross_wrong_not_offensive_input = base_olid + "in_correct_cross_wrong_not_offensive.csv"

inputfile_off = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/wordlists/all_caps.tsv"
df_off = pd.read_csv(inputfile_off, sep="\t")

df_easy = pd.read_csv(easy_instances_input, sep=",", index_col=[0])
df_easy_offensive = pd.read_csv(easy_offensive_instances_input, sep=",", index_col=[0])
df_easy_not_offensive = pd.read_csv(easy_not_offensive_instances_input, sep=",", index_col=[0])

df_hard = pd.read_csv(hard_instances_input, sep=",", index_col=[0])
df_hard_offensive = pd.read_csv(hard_offensive_instances_input, sep=",", index_col=[0])
df_hard_not_offensive = pd.read_csv(hard_not_offensive_instances_input, sep=",", index_col=[0])

df_cross_correct_in_wrong =  pd.read_csv(cross_correct_in_wrong_input, sep=",", index_col=[0])
df_cross_correct_in_wrong_offensive = pd.read_csv(cross_correct_in_wrong_offensive_input,  sep=",", index_col=[0])
df_cross_correct_in_wrong_not_offensive = pd.read_csv(cross_correct_in_wrong_not_offensive_input,  sep=",", index_col=[0])

df_in_correct_cross_wrong =  pd.read_csv(in_correct_cross_wrong_input, sep=",", index_col=[0])
df_in_correct_cross_wrong_offensive = pd.read_csv(in_correct_cross_wrong_offensive_input, sep=",", index_col=[0])
df_in_correct_cross_wrong_not_offensive = pd.read_csv(in_correct_cross_wrong_not_offensive_input, sep=",", index_col=[0])


def length(df):
    len_count = 0
    total_count = 0
    for index, row in df.iterrows():
        len_count += len(row["text"])
        total_count +=1
    print(len_count)
    print(total_count)

def no_offensive_words(df):
    #used to count instances
    count = 0
    #used to make dataframe later
    a_list = []
    #find offensive word per text instance
    for a in df["text"]:
        for index, row in df_off.iterrows():
            if row["original"] in a:
                a = a.replace(row["original"], row["new"])
                #count
                count += 1
    print("number of offensive words:", count)

length(df_in_correct_cross_wrong_not_offensive)
no_offensive_words(df_in_correct_cross_wrong_not_offensive)
