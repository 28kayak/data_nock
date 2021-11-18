"""[CH2: 揺れがあるまま集計する]
The Data going to use: data/ch2
"""
import pandas as pd
# read csv data
gross_data = pd.read_csv('./data/ch2/uriage.csv')
# read excel data
client_data = pd.read_excel('./data/ch2/kokyaku_daicho.xlsx')

gross_data['purchase_date'] = pd.to_datetime(gross_data["purchase_date"])
gross_data['purchase_month'] = gross_data["purchase_date"].dt.strftime("%Y%m")
res = gross_data.pivot_table(
    index='purchase_month',
    columns='item_name',
    aggfunc='size',
    fill_value=0)
print(res)

res1 = gross_data.pivot_table(
    index="purchase_month",
    columns='item_name',
    values='item_price',
    aggfunc='sum',
    fill_value=0
)
print(res1)