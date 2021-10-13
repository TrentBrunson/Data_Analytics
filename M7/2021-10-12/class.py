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
mortality_data.values
# %%
print("Index:  ", mortality_data.index)
print("Columns:", mortality_data.columns)
print("Size:   ", mortality_data.size)
print("Shape:  ", mortality_data.shape)
# %%
# Justices
justices_data.shape
justices_data.index
justices_data.values
# %%
justiceList
# %%
mortality_data.info()
# %%
mortality_data.nunique()
# %%
mortality_data.describe()
# %%
mortality_data.describe().T
#%%
mortality_data.values
#%%
mortality_data.columns
#%%
mortality_data.rename(columns={"Death Rate":"DeathRate","Age Group":"AgeGroup"}, inplace=True)
# mortality_data.columns = mortality_data.columns.str.replace(' ','')
mortality_data.columns
# %%
# Access the data
# %%
mortality_data.DeathRate.head(2)
# %%
type(mortality_data.DeathRate)
# %%
mortality_data['DeathRate'].head(2)
# %%
mortality_data[['Year','DeathRate']].head(2)
# %%
type(mortality_data[['Year','DeathRate']])
# %%
# Access Rows
# %%
mortality_data.query('Year==1900')
# %%
mortality_data.query('Year == 2000 and AgeGroup != "1-4 Years"')
# %%
mortality_data.query('Year == 1900 or Year == 2000')
# %%
# Access subset of rows
# %%
mortality_data.loc[[0,5,10]]
#%%
mortality_data.loc[4:60]
# %%
mortality_data.loc[0:110:10]
# %%
mortality_data.loc[mortality_data.Year == 1917]
# %%
# loc looks for rows to retrieve and then columns to retrieve lists
mortality_data.loc[:, ['Year', 'AgeGroup']]
# %%
# loc looks for rows to retrieve and then columns to retrieve lists
mortality_data.loc[[0,5,10],['AgeGroup','DeathRate']]
# %%
# loc looks for rows to retrieve and then columns to retrieve lists
mortality_data.loc[4:6,'AgeGroup':'DeathRate']
# %%
# access rows 0, 5, and 10 see cell above with mortality_data.loc[[0,5,10]] for comparison
mortality_data.iloc[[0,5,10]]
# %%
mortality_data.iloc[[4,5,6],[1,2]]
# %%
mortality_data.iloc[[4,5,6],[0,2]]
# %%
mortality_data.iloc[4:7,1:3]
# %%
mortality_data.iloc[-10:]
# %%
# Prepare the data
# %%
# sorting
# %%
mortality_data.sort_values('DeathRate', ascending=False).head(3)
# %%
mortality_data.sort_values(['Year','DeathRate']).head(30)
# %%
mortality_data.sort_values(['Year','DeathRate'],ascending=[True,False]).head()
# %%
# Statistical methods
# %%
mortality_data.DeathRate.mean()
# %%
mortality_data[['AgeGroup','DeathRate']].max()
# %%
mortality_data.count()
# %%
mortality_data.quantile([.1,.25,.5,.75,.9])
# %%
mortality_data.DeathRate.cumsum()
# %%
mortality_data['MeanCentered'] = mortality_data.DeathRate - mortality_data.DeathRate.mean()
mortality_data
# %%
mortality_data['DeathRate'] = mortality_data.DeathRate / 100000
mortality_data
#%%
justices_data.rename(
    columns={'Year Appointed':'YearAppointed',
    'Year Left Court':'YearLeftCourt'}, inplace=True
    )
justices_data['YearsServed'] = justices_data.YearLeftCourt - justices_data.YearAppointed
justices_data
#%%
justices_data
# %%
# manipulate data in column
# with strings
# %%
mortality_data.AgeGroup.replace(
    to_replace = ['1-4 Years','5-9 Years'],
    value = ['01-04 Years','05-09 Years'],
    inplace = True)
mortality_data
# %%
mortality_data.AgeGroup.replace(
    {'1-4 Years':'01-04 Years','5-9 Years':'05-09 Years'},
    inplace = True)
mortality_data
# %%
# Shape the DF
# %%
mortality_data.set_index('Year', inplace=True)
mortality_data
# %%
mortality_data.reset_index(inplace=True)
# %%
mortality_data = mortality_data.set_index('Year', verify_integrity=True)
# code error because keys for new index are not unique
# %%
mortality_data = mortality_data.set_index(['Year','AgeGroup'], verify_integrity=True)
mortality_data
# %%
mortality_data.reset_index(inplace = True)
# %%
mortality_wide = mortality_data.pivot(index='Year', columns='AgeGroup', values='DeathRate')
mortality_wide
# %%
# Melting the data (wide-to-long)
# %%
# get starting data
mortality_wide = mortality_data.pivot(index='Year', columns='AgeGroup', values='DeathRate')

# save to Excel format to remove indexes
mortality_wide.to_excel('mortality_wide.xlsx')
mortality_wide = pd.read_excel('mortality_wide.xlsx')

mortality_wide
# %%
mortality_long = mortality_wide.melt(
    id_vars = 'Year',
    value_vars=['01-04 Years','05-09 Years'],
    var_name ='AgeGroup',
    value_name='DeathRate')

with pd.option_context('display.max_rows', 4):
    display(mortality_long)
# %%
# Analyze data
# %%
# Grouping data
# %%
mortality_data.groupby('AgeGroup').mean()
# %%
mortality_data.groupby('Year').median()
# %%
mortality_data.groupby(['Year','AgeGroup']).count()
# %%
# Aggregate the data
# %%
mortality_data.groupby('AgeGroup').agg(['mean','median'])
# %%
mortality_data.groupby('AgeGroup')['DeathRate'].agg(['mean','median','std','unique'])
# %%
mortality_data.groupby('AgeGroup')['DeathRate'].agg(['mean','median','std','nunique'])
# %%
mortality_data.groupby('Year')['DeathRate'].agg(
    ['mean','median','std','min','max','var','nunique'])
# %%
# Visualize
# %%
mortality_data.pivot(index='Year',columns='AgeGroup')['DeathRate'].plot()
# %%
mortality_data.groupby('AgeGroup')['DeathRate'].agg(['mean','median','std']
).plot.barh(legend='reverse')
# %%
