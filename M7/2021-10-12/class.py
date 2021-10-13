#%%
import pandas as pd
# %%
file = 'mortality.csv'
mortality_data = pd.read_csv(file)
#%%
mortality_data
# %%
url = 'https://data.cdc.gov/api/views/v6ab-adf5/rows.csv?accessType=DOWNLOAD'
mortality_data = pd.read_csv(url)
# %%
df_data=[[1900, '1-4 Years', 1983.8],
         [1901, '1-4 Years', 1695.0]]
df_columns=['Year', 'Age Group', 'Death Rate']
# %%
mortality_df = pd.DataFrame(
    data=df_data,
    columns=df_columns)
# %%
mortality_df
# %%
with open('justices.txt', 'r') as infile:
    justiceList = [line.rstrip() for line in infile]
print(justiceList)
# %%
for i in range(len(justiceList)):
    justiceList[i] = justiceList[i].split(',')
    justiceList[i][4] = int(justiceList[i][4])
    justiceList[i][5] = int(justiceList[i][5])
    # set 'Year Left Court' for current justices
    if justiceList[i][5] == 0:
        justiceList[i][5] = 2021
justiceList
# %%
justice_df_data = justiceList
justice_df_columns = ['First Name','Last Name','Appointed By','Home State','Year Appointed','Year Left Court']
# %%
justices_data = pd.DataFrame(data=justice_df_data, columns=justice_df_columns)
# %%
justices_data
#%%
# Save and restore the data
# %%
mortality_data.to_pickle('mortality_data.pkl')
# %%
mortality_data = pd.read_pickle('mortality_data.pkl')
# %%
mortality_data.head()
# %%
justices_data.to_pickle('justices_data.pkl')
# %%
justices_data = 'empty'
justices_data
# %%
justices_data = pd.read_pickle('justices_data.pkl')
justices_data
# %%
# Examine and clean data
# %%
mortality_data
# %%
with pd.option_context('display.max_rows', 5,'display.max_columns', None):
    display(mortality_data)
# %%
mortality_data.head(9)
# %%
mortality_data.tail(6)
# %%
# Display DF
# %%
