import pandas as pd

#inputfiles
base_olid = "data/1_results_OLID/"
in_domain = "in-domain/"
cross_domain = "cross-domain/"


inputfile_in_domain_olid = base_olid +in_domain+"in_domain_OLID_test_predicted.csv"
inputfile_cross_domain_olid = base_olid +cross_domain+"cross_domain_OLID_test_predicted.csv"

df_in = pd.read_csv(inputfile_in_domain_olid, sep=",", index_col=[0])
df_cross = pd.read_csv(inputfile_cross_domain_olid, sep=",", index_col=[0])

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

df_in["cross_predicted"] = df_cross["predicted"]


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

    #itterate over rows in df
    for index, row in df_in.iterrows():
        #Right predicitons in-domain
        if row["predicted"] == row["labels"]:
            if row["predicted"] == 1:
                count_in_off_good += 1
            if row["predicted"] == 0:
                count_in_not_good += 1
            #See if right predictions in-domain overlap with cross-domain
            if row["predicted"] == row["cross_predicted"]:
                count_same_good += 1
                # if overlap, count overlap in offensive instances and in not offensive instances
                if row["predicted"] == 1:
                    count_same_good_off +=1
                elif row["predicted"] == 0:
                    count_same_good_not += 1
            else:
                #count the number where in-domain is right and cross_domain is wrong
                count_in_right_cross_wrong += 1
                if row["predicted"] == 1:
                    count_in_right_cross_wrong_off += 1
                if row["predicted"] == 0:
                    count_in_right_cross_wrong_not += 1
        #wrong predictions
        if row["predicted"] != row["labels"]:
            if row["labels"] == 1:
                false_negative_in += 1
            if row["labels"] == 0:
                false_positive_in += 1
            #wrong predictions overlap
            if row["predicted"] == row["cross_predicted"]:
                count_same_false += 1
                #overlap wrong predictions, OFF and NOT
                if row["labels"] == 1:
                    count_same_false_off +=1
                elif row["labels"] == 0:
                    count_same_false_not += 1
        # right predictions cross, wrong predicitons in-domain
        if row["cross_predicted"] == row["labels"]:
            if row["cross_predicted"] == 1:
                count_cross_off_good += 1
            if row["cross_predicted"] == 0:
                count_cross_not_good += 1
            if row["labels"] != row["predicted"]:
                count_cross_right_in_wrong += 1
                if row["cross_predicted"] == 1:
                    count_cross_right_in_wrong_off += 1
                elif row["cross_predicted"] == 0:
                    count_cross_right_in_wrong_not += 1
        if row["cross_predicted"] != row["labels"]:
            if row["labels"] == 1:
                false_negative_cross += 1
            if row["labels"] == 0:
                false_positive_cross += 1


    print("\n")
    print("count_same_false :", count_same_false)
    print("Of which are:")
    print("count_same_false_off:", count_same_false_off)
    print("count_same_false_not:", count_same_false_not)

    print("\n")
    print("count_same_good :", count_same_good )
    print("Of which are:")
    print("count_same_good_off :", count_same_good_off )
    print("count_same_good_not  :", count_same_good_not )

    print("\n")
    print("count_in_right_cross_wrong:", count_in_right_cross_wrong )
    print("Of which are:")
    print("count_in_right_cross_wrong_off :", count_in_right_cross_wrong_off)
    print("count_in_right_cross_wrong_not  :", count_in_right_cross_wrong_not )

    print("\n")
    print("count_cross_right_in_wrong :", count_cross_right_in_wrong )
    print("Of which are:")
    print("count_cross_right_in_wrong_not:", count_cross_right_in_wrong_not)
    print("count_cross_right_in_wrong_off:", count_cross_right_in_wrong_off)

    print("\n")
    print("in-domain right predictions:")
    print("Of which are:")
    print("count_in_off_good", count_in_off_good)
    print("count_in_not_good ", count_in_not_good)

    print("\n")
    print("cross-domain right predictions:")
    print("Of which are:")
    print("count_cross_off_good:", count_cross_off_good)
    print("count_cross_not_good:", count_cross_not_good)

    print("\n")
    print("in-domain wrong predictions:")
    print("Of which are:")
    print("false_negative_in :", false_negative_in )
    print("false_positive_in:", false_positive_in)

    print("\n")
    print("cross-domain wrong predictions:")
    print("Of which are:")
    print("false_negative_cross :", false_negative_cross )
    print("false_positive_cross:", false_positive_cross)

#wrong_predict_base(df_in)
in_vs_cross(df_in)
