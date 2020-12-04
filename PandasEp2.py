import pandas as pd
import matplotlib.pyplot as plt
cereal_df = pd.read_csv("flights.csv")
transD_pd = pd.DataFrame(cereal_df)
NimbleCount = transD_pd[transD_pd.CARGO == "Nimble"].count().CARGO
NimbleMoney = transD_pd[transD_pd.CARGO == "Nimble"]["PRICE"].sum()
NimbleVes = transD_pd[transD_pd.CARGO == "Nimble"]["WEIGHT"].sum()
JumboCount = transD_pd[transD_pd.CARGO == "Jumbo"].count().CARGO
JumboMoney = transD_pd[transD_pd.CARGO == "Jumbo"]["PRICE"].sum()
JumboVes = transD_pd[transD_pd.CARGO == "Jumbo"]["WEIGHT"].sum()
MediumCount = transD_pd[transD_pd.CARGO == "Medium"].count().CARGO
MediumMoney = transD_pd[transD_pd.CARGO == "Medium"]["PRICE"].sum()
MediumVes = transD_pd[transD_pd.CARGO == "Medium"]["WEIGHT"].sum()
print(NimbleCount)
data = {'Weight': [NimbleVes, JumboVes, MediumVes],
        'Cash': [NimbleMoney, JumboMoney, MediumMoney],
        'Deals': [NimbleCount, JumboCount, MediumCount]}
df = pd.DataFrame(data)
df.plot(kind='bar')
plt.xticks(range(3),['Nimble','Jumbo','Medium'])
plt.show()