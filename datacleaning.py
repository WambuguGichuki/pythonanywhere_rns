from operator import concat
import pandas as pd
import datetime as dt
from gstring import expense_df,sales_df,newsales_df,newexpense_df,ordertime_df

# incomes = pd.read_csv('dash-table-income.csv')

# expenses = pd.read_csv('dash-table-expenses.csv')


# sales = incomes[['date ordered','Total spent','month','week']]

# expense = expenses[['Input expense amount','Input expense date','month','week']]

# sales = sales.rename(columns={'date ordered':'date'})
# expense = expense.rename(columns={'Input expense date':'date','Input expense amount':'expense amount'})

# sales = sales.fillna(0)
# expense = expense.fillna(0)



# cashflow = pd.merge(sales,expense,on = ['date'],how='outer')
# cashflow = cashflow.fillna(0)
# cashflow['cashflow'] = cashflow['Total spent'] - cashflow['expense amount']


##  SALES DATA-CLEANING
sales_df = sales_df.drop(['Timestamp'],axis=1)
new_newsales_df = newsales_df.drop(['Timestamp','Order number (Format (#d/m/y/0000) day(6)/month(4)/year(22)/number(0001)) number resets each new day','Time ordered','product ordered type','Toppings/options included [bacon]',
                                'Toppings/options included [grilled onions]','Toppings/options included [fries]'],axis=1)

new_newsales_df['customer phone'] = '0' + new_newsales_df['customer phone'].astype('str')

concat_df = pd.concat([sales_df,new_newsales_df],ignore_index=True)



# concat_df['customer phone'] = concat_df['customer phone'].astype('str')
concat_df['Total spent'] = pd.to_numeric(concat_df['Total spent'])




concat_df['customer name'] = concat_df['customer name'].str.lower()

concat_df['date ordered'] = pd.to_datetime(concat_df['date ordered'])

concat_df = concat_df.rename(columns = {'Total spent':'Total','date ordered':'date'})

concat_df['month'] = concat_df['date'].dt.strftime('%Y-%m')
concat_df['week'] = concat_df['date'].dt.to_period('w').astype('str')#.strftime('%U')#.apply(lambda x: '{0}-{1}'.format(x.year, x.strftime('%W')))
concat_df['year'] = concat_df['date'].dt.year

# sales_df[['month','week']] = pd.to_datetime(sales_df[['month','week']])



concat_df['Total'] = concat_df['Total'].fillna(0)

concat_df[['Product ordered quantity [solo-man]','Product ordered quantity [twin-pack]','Product ordered quantity [sherehe-pack]']] = concat_df[['Product ordered quantity [solo-man]','Product ordered quantity [twin-pack]','Product ordered quantity [sherehe-pack]']].apply(pd.to_numeric)
concat_df[['Product ordered quantity [solo-man]','Product ordered quantity [twin-pack]','Product ordered quantity [sherehe-pack]']] = concat_df[['Product ordered quantity [solo-man]','Product ordered quantity [twin-pack]','Product ordered quantity [sherehe-pack]']].fillna(0)
concat_df['total burgers'] = (concat_df['Product ordered quantity [solo-man]'] + (concat_df['Product ordered quantity [twin-pack]'] * 2) + (concat_df['Product ordered quantity [sherehe-pack]'] * 4))




cleanedsales_df = concat_df[['date','Total','month','week','total burgers']]

def total_cust(period):
    time = concat_df[concat_df['month'] <= period]
    return time['customer phone'].nunique()


months = concat_df['month'].unique()

uniquemonths = pd.DataFrame({'month': [i for i in months]})

uniquemonths['cust count'] = uniquemonths['month'].apply(total_cust)
uniquecust = concat_df.groupby('month')['customer phone'].nunique().reset_index()
monthlyorders = concat_df.groupby('month')['Total'].count().reset_index()
monthlysales = concat_df.groupby('month')['Total'].sum().reset_index()

merge1 = pd.merge(uniquemonths,uniquecust,on='month')
merge2 = pd.merge(merge1,monthlyorders,on='month')
merged_df = pd.merge(merge2,monthlysales,on = 'month')
merged_df = merged_df.rename(columns = {'Total_x':'total_orders','Total_y':'total_sales','customer phone':'unique customers'})

merged_df['new customers'] = merged_df['cust count'].diff()
merged_df['reorder customers'] = merged_df['unique customers'] - merged_df['new customers']

merged_df['reorder customers'] = merged_df['reorder customers'].shift(-1)
merged_df['reorder rate'] = round((merged_df['reorder customers']/merged_df['cust count'])*100)

merged_df['avgsale_per_order'] = round(merged_df['total_sales']/merged_df['total_orders'])
merged_df['avgsale_per_cust'] = round(merged_df['total_sales']/merged_df['unique customers'])


merged_df['reorder customers'] = merged_df['reorder customers'].shift(1)
merged_df['reorder rate'] = merged_df['reorder rate'].shift(1)


merged_df = merged_df.fillna(0)



total_customers = merged_df['cust count'].iloc[-1]
# print(total_customers)
# print(merged_df)

#####  *********** EXPENSES DATA CLEANING ************  ##########

expense_df = expense_df.drop(['Timestamp','Input expense description'],axis = 1)
new_newexpense_df = newexpense_df.drop(['Timestamp','input expense description','input expense type'],axis=1) 

def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df

new_newexpense_df = swap_columns(new_newexpense_df,'Input expense item','Input expense amount')



concat_expense_df = pd.concat([expense_df,new_newexpense_df],ignore_index=True)

concat_expense_df['Input expense amount'] = pd.to_numeric(concat_expense_df['Input expense amount'])

concat_expense_df['Input expense date'] = pd.to_datetime(concat_expense_df['Input expense date'])

concat_expense_df = concat_expense_df.rename(columns= {'Input expense date':'date','Input expense amount':'expense amount','Input expense item':'expense item'})

concat_expense_df['expense item'] = concat_expense_df['expense item'].str.lower()

concat_expense_df['month'] = concat_expense_df['date'].dt.strftime('%Y-%m')
concat_expense_df['week'] = concat_expense_df['date'].dt.to_period('w').astype('str')#strftime('%U')#apply(lambda x: '{0}-{1}'.format(x.year, x.strftime('%W')))
concat_expense_df['year'] = concat_expense_df['date'].dt.year

concat_expense_df['expense amount'] = concat_expense_df['expense amount'] * -1


cleanedexpense_df = concat_expense_df[['expense amount','date','month','week']]
# print(cleanedexpense_df)
