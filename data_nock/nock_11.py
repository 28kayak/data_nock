"""[CH2: 小売店のデータで加工を行う]
The Data going to use: data/ch2
"""
import pandas as pd
# read data from csv
gross_sale = pd.read_csv('./data/ch2/uriage.csv')
# read data from Excel file
client_data = pd.read_excel('./data/ch2/kokyaku_daicho.xlsx')

print(gross_sale.head())
print(client_data.head())
"""[nock_12: データの揺れを確認する]
日付データ・名前・item_name
---
    purchase_date item_name  item_price customer_name
0  2019-06-13 18:02:34       商品A       100.0         深井菜々美
1  2019-07-13 13:05:29     商 品 S         NaN          浅田賢二
2  2019-05-11 19:42:07     商 品 a         NaN          南部慶二
3  2019-02-12 23:40:45       商品Z      2600.0          麻生莉緒
4  2019-04-22 03:09:35       商品a         NaN          平田鉄二
      顧客名        かな  地域                     メールアドレス         登録日
0   須賀ひとみ    すが ひとみ  H市     suga_hitomi@example.com  2018/01/04
1  岡田　 敏也   おかだ としや  E市   okada_toshiya@example.com       42782
2    芳賀 希    はが のぞみ  A市     haga_nozomi@example.com  2018/01/07
3   荻野  愛    おぎの あい  F市        ogino_ai@example.com       42872
4   栗田 憲一  くりた けんいち  E市  kurita_kenichi@example.com       43127
"""
print(gross_sale['item_name'].head())
print(gross_sale['item_price'].head())