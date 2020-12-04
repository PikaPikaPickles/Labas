import pandas as pd
cereal_df = pd.read_csv("transactions.csv")
transD_pd = pd.DataFrame(cereal_df)
print(sorted(transD_pd[transD_pd.STATUS == "OK"].SUM, reverse=True)[0:3])
hj = (transD_pd[transD_pd.STATUS == "OK"])
print((hj[hj.CONTRACTOR == "Umbrella, Inc"]["SUM"].sum()))