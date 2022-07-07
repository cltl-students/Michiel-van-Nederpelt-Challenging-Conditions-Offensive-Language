import pandas as pd

#inputfiles
base_olid = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/1_results_OLID/"
base_hasoc = "/Users/michielv.nederpelt/Desktop/Studie/Thesis/data/1_results_HASOC/"
in_domain = "in-domain/"
cross_domain = "cross-domain/"

hasoc= base_hasoc +in_domain+"in_domain_HASOC_test_predicted.csv"
inputfile_perturbed = base_hasoc +in_domain+ "in_domain_HASOC_perturbed_a_to_star_test_predicted.csv"
df_in = pd.read_csv(hasoc, sep=",", index_col=[0])
df_perturb = pd.read_csv(inputfile_perturbed, sep=",", index_col=[0])

df_in["perturbed-predicted"] = df_perturb["predicted"]

def wrong_predict(df_in):
    count=0
    for index, row in df_in.iterrows():
        if row["predicted"] != row["perturbed-predicted"]:
            count +=1
    print(count)

wrong_predict(df_in)
