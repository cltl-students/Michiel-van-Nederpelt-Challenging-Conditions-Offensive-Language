#imports
import pandas as pd


def wrong_predict_base(df_in):
    count_wrong=0
    count_wrong1 = 0
    count_wrong0 = 0
    print(df_in)
    for index, row in df_in.iterrows():
        if row["labels"] != row["predicted"] :
            count_wrong +=1
            if row["labels"] == 1:
                count_wrong1 +=1
            else:
                count_wrong0 +=1
    print("total wrong:", count_wrong)
    print("offensive wrong:", count_wrong1)
    print("not offensive wrong:", count_wrong0)

#______________________________________________________________________________

def in_vs_cross(df_in):
    count_wrong=0
    count_wrong1 = 0
    count_wrong0 = 0
    count_cross_right_in_wrong = 0
    count_cross_right_in_wrong_not = 0
    count_cross_right_in_wrong_off = 0
    count_same_false_not =0
    count_same_false_off = 0
    count_same_false = 0
    count_same_good =0
    count_same_good_off =0
    count_same_good_not = 0
    count_in_right_cross_wrong =0
    count_in_right_cross_wrong_off =0
    count_in_right_cross_wrong_not =0
    count_in_off_good = 0
    count_in_not_good = 0
    count_cross_off_good = 0
    count_cross_not_good = 0
    false_negative_cross = 0
    false_positive_cross = 0
    false_negative_in = 0
    false_positive_in = 0
    agreed_offensive_correct_list =[]
    agreed_notoffensive_correct_list = []
    agreed_correct_list = []
    agreed_wrong_list = []
    agreed_wrong_notoffensive_list = []
    agreed_wrong_offensive_list = []
    cross_correct_in_wrong_list = []
    cross_correct_in_wrong_offensive_list = []
    cross_correct_in_wrong_not_offensive_list = []
    in_correct_cross_wrong_list = []
    in_correct_cross_wrong_offensive_list =[]
    in_correct_cross_wrong_not_offensive_list = []
    #itterate over rows in df
    for index, row in df_in.iterrows():
        #Right predicitons in-domain
        if row["predicted"] == row["labels"]:
            if row["predicted"] == row["cross_predicted"]:
                count_same_good += 1
                agreed_correct_list.append(row)
                # if overlap, count overlap in offensive instances and in not offensive instances
                if row["predicted"] == 1:
                    count_same_good_off +=1
                    agreed_offensive_correct_list.append(row)
                elif row["predicted"] == 0:
                    count_same_good_not += 1
                    agreed_notoffensive_correct_list.append(row)
            else:
                #count the number where in-domain is right and cross_domain is wrong
                count_in_right_cross_wrong += 1
                in_correct_cross_wrong_list.append(row)
                if row["predicted"] == 1:
                    count_in_right_cross_wrong_off += 1
                    in_correct_cross_wrong_offensive_list.append(row)
                if row["predicted"] == 0:
                    count_in_right_cross_wrong_not += 1
                    in_correct_cross_wrong_not_offensive_list.append(row)
        #wrong predictions
        if row["predicted"] != row["labels"]:
            if row["predicted"] == row["cross_predicted"]:
                count_same_false += 1
                agreed_wrong_list.append(row)
                #overlap wrong predictions, OFF and NOT
                if row["labels"] == 1:
                    count_same_false_off +=1
                    agreed_wrong_offensive_list.append(row)
                elif row["labels"] == 0:
                    count_same_false_not += 1
                    agreed_wrong_notoffensive_list.append(row)
        # right predictions cross
        if row["cross_predicted"] == row["labels"]:
            if row["cross_predicted"] == 1:
                count_cross_off_good += 1
            if row["cross_predicted"] == 0:
                count_cross_not_good += 1
            #right predictions cross, wrong predictions in
            if row["labels"] != row["predicted"]:
                count_cross_right_in_wrong += 1
                cross_correct_in_wrong_list.append(row)
                if row["cross_predicted"] == 1:
                    count_cross_right_in_wrong_off += 1
                    cross_correct_in_wrong_offensive_list.append(row)
                elif row["cross_predicted"] == 0:
                    count_cross_right_in_wrong_not += 1
                    cross_correct_in_wrong_not_offensive_list.append(row)
        if row["cross_predicted"] != row["labels"]:
            if row["labels"] == 1:
                false_negative_cross += 1
            if row["labels"] == 0:
                false_positive_cross += 1
                #convert all to dataframe
    df_correct = pd.DataFrame(agreed_correct_list, columns = ["text", "labels", "predicted", "cross_predicted"])
    df_correct_offensive = pd.DataFrame(agreed_offensive_correct_list, columns = ["text", "labels", "predicted", "cross_predicted"])
    df_correct_notoffensive = pd.DataFrame(agreed_notoffensive_correct_list, columns = ["text", "labels", "predicted", "cross_predicted"])
    print(df_correct)

    #in_vs_cross
    df_cross_correct_in_wrong = pd.DataFrame(cross_correct_in_wrong_list , columns = ["text", "labels", "predicted", "cross_predicted"])
    df_cross_correct_in_wrong_offensive = pd.DataFrame(cross_correct_in_wrong_offensive_list , columns = ["text", "labels", "predicted", "cross_predicted"])
    df_cross_correct_in_wrong_not_offensive = pd.DataFrame(cross_correct_in_wrong_not_offensive_list  , columns = ["text", "labels", "predicted", "cross_predicted"])
    df_in_correct_cross_wrong = pd.DataFrame(in_correct_cross_wrong_list , columns = ["text", "labels", "predicted", "cross_predicted"])
    df_in_correct_cross_wrong_offensive = pd.DataFrame(in_correct_cross_wrong_offensive_list  , columns = ["text", "labels", "predicted", "cross_predicted"])
    df_in_correct_cross_wrong_not_offensive = pd.DataFrame(in_correct_cross_wrong_not_offensive_list , columns = ["text", "labels", "predicted", "cross_predicted"])

    df_incorrect = pd.DataFrame(agreed_wrong_list, columns = ["text", "labels", "predicted", "cross_predicted"])
    df_incorrect_offensive = pd.DataFrame(agreed_wrong_offensive_list, columns = ["text", "labels", "predicted", "cross_predicted"])
    df_incorrect_notoffensive = pd.DataFrame(agreed_wrong_notoffensive_list, columns = ["text", "labels", "predicted", "cross_predicted"])


    df_correct.to_csv(easy_instances_output, sep="\t")
    df_correct_offensive.to_csv(easy_instances_offensive_output, sep="\t")
    df_correct_notoffensive .to_csv(easy_instances_notoffensive_output, sep="\t")

    df_incorrect.to_csv(hard_instances_output, sep="\t")
    df_incorrect_offensive.to_csv(hard_instances_offensive_output, sep="\t")
    df_incorrect_notoffensive.to_csv(hard_instances_notoffensive_output, sep="\t")

    df_cross_correct_in_wrong.to_csv(cross_correct_in_wrong_out, sep="\t")
    df_cross_correct_in_wrong_offensive.to_csv(cross_correct_in_wrong_offensive_out, sep="\t")
    df_cross_correct_in_wrong_not_offensive.to_csv(cross_correct_in_wrong_not_offensive_out, sep="\t")
    df_in_correct_cross_wrong.to_csv(in_correct_cross_wrong_out, sep="\t")
    df_in_correct_cross_wrong_offensive.to_csv(in_correct_cross_wrong_offensive_out, sep="\t")
    df_in_correct_cross_wrong_not_offensive.to_csv(in_correct_cross_wrong_not_offensive_out, sep="\t")


#inputfiles basic paths
base_olid = "data/1_results_OLID/"
base_hasoc = "data/1_results_HASOC/"
in_vs_cross_out = "in_vs_cross/"
in_domain = "in-domain/"
cross_domain = "cross-domain/"

#inputfiles extended paths
inputfile_in_domain_hasoc = base_hasoc +in_domain+"in_domain_hasoc_test_predicted.csv"
inputfile_cross_domain_hasoc = base_hasoc+cross_domain+"cross_domain_hasoc_test_predicted.csv"

#outpurfiles
easy_instances_output = base_hasoc + in_vs_cross_out + "correct_easy_predicitions.tsv"
easy_instances_offensive_output = base_hasoc+ in_vs_cross_out + "correct_offensive_easy_predicitions.tsv"
easy_instances_notoffensive_output = base_hasoc +in_vs_cross_out+ "correct_notoffensive_easy_predicitions.tsv"

hard_instances_output = base_hasoc + in_vs_cross_out + "wrong_hard_predicitions.tsv"
hard_instances_offensive_output = base_hasoc + in_vs_cross_out + "wrong_offensive_hard_predicitions.tsv"
hard_instances_notoffensive_output = base_hasoc +in_vs_cross_out+ "wrong_notoffensive_hard_predicitions.tsv"

cross_correct_in_wrong_out = base_hasoc + in_vs_cross_out + "cross_correct_in_wrong.tsv"
cross_correct_in_wrong_offensive_out = base_hasoc + in_vs_cross_out + "cross_correct_in_wrong_offensive.tsv"
cross_correct_in_wrong_not_offensive_out =base_hasoc + in_vs_cross_out + "cross_correct_in_wrong_not_offensive.tsv"
in_correct_cross_wrong_out = base_hasoc+ in_vs_cross_out + "in_correct_cross_wrong.tsv"
in_correct_cross_wrong_offensive_out = base_hasoc + in_vs_cross_out + "in_correct_cross_wrong_offensive.tsv"
in_correct_cross_wrong_not_offensive_out = base_hasoc + in_vs_cross_out + "in_correct_cross_wrong_not_offensive.tsv"

#make dataframes
df_in = pd.read_csv(inputfile_in_domain_hasoc, sep=",", index_col=[0])
df_cross = pd.read_csv(inputfile_cross_domain_hasoc, sep=",", index_col=[0])

#add predicted column dataframe cross-domain in df in-domain
df_in["cross_predicted"] = df_cross["predicted"]


#wrong_predict_base(df_in)
in_vs_cross(df_in)
