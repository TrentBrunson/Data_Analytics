#%%
import pandas as pd
# %%
df_data=[[1900,'1-4 Years', 1983.8],[1901, '1-4 Years', 1695.0]]
df_columns = ['Year', 'Age Group', 'Death Rate']
#%%
mortalityDF = pd.DataFrame(data=df_data, columns=df_columns)
# %%
mortalityDF
# %%
