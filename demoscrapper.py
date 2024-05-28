# from random import randint
# from time import sleep
# import requests
# from bs4 import BeautifulSoup


# totalshare=[]

# URL = "https://www.moneycontrol.com/financials/mindtree/balance-sheetVI/MT13"
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# }
# page = requests.get(URL, headers=headers)
# soup = BeautifulSoup(page.text, 'html.parser')

# table = soup.find("table", { "class" : "mctable1" })
  
# for row in table.findAll("tr"):
#     cells = row.findAll("td")
#     totalshare.append(cells)
#     # print (totalshare)

# # print(type(totalshare[14]))

# # print(type(cells))

# if pd.read_html does not work, we can use pd.read_html using requests.
import pandas as pd
import requests

# url = "https://www.moneycontrol.com/financials/mindtree/capital-structure/MT13#MT13"

# # r = requests.get(url)
# # df_list = pd.read_html(r.text)
# # print(df_list)
# # df = df_list[0]
# # df.info()
# # print(df_list)
# # Total_number_of_share=df_list[0][('- P A I D U P -', 'Shares (nos)')][0]
# # print(Total_number_of_share)

# url = "https://www.moneycontrol.com/financials/mindtree/balance-sheetVI/MT13"

# r = requests.get(url)
# df_list = pd.read_html(r.text)
# # print(df_list[0])
# Total_non_current_liability = df_list[0][(1)][(14)]
# print(Total_non_current_liability)
# # df = df_list[0]
# # df.info()

url = "https://www.moneycontrol.com/financials/mindtree/ratiosVI/MT13"
r = requests.get(url)
df_list = pd.read_html(r.text)
print((df_list[0][(1)][(32)]))

