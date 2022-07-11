import pandas as pd

#inputfiles
base_olid = "data/results_OLID_test/"
base_hasoc = "data/results_HASOC_test/"
in_domain = "in-domain/"
cross_domain = "cross-domain/"

inputfile_in_domain_olid = base_olid +in_domain+"OLID_train_OLID__test_predicted.csv"
inputfile_cross_domain_olid = base_olid +cross_domain+"HASOC_train_OLID__test_predicted.csv"
#outputfiles:
outputputfile_in_domain_olid = base_olid+ in_domain +"wrong_predictions/OLID_train_OLID_test_wrong_predictions.csv"
outputputfile_cross_domain_olid = base_olid+ cross_domain +"wrong_predictions/HASOC_train_OLID_test_wrong_predictions.csv"


def wrong_predictions(inputfile, outputfile):
    df = pd.read_csv(inputfile, sep=",", index_col=[0])
    df_wrong_pred = pd.DataFrame(columns = ["text", "labels", "predicted"])
    count = 0
    for index, row in df.iterrows():
            if row["labels"] != row["predicted"]:
                count += 1
                df_wrong_pred = df_wrong_pred.append(row)
    print(count)
    print(df_wrong_pred)
    df_wrong_pred.to_csv(outputfile)

wrong_predictions(inputfile_cross_domain_olid, outputputfile_cross_domain_olid)


#inputfile_in_domain_hasoc =
inputfile_cross_domain_hasoc = "data/results_HASOC_test/in-domain/OLID_train_HASOC__test_predicted.csv"
#inputfile_cross_domain_olid =
