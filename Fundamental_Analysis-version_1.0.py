#------------------Manually Inputs ---------------------------
import datetime as dt
today = dt.date.today()
Present_year = int(today.strftime("%Y"))

#INPUTS -----------------------------------------------------------------------------------------------------------------------
# Taking Enterprise Values of past year in crores
Present_year_Enterprise_value = float(input(f"Enterpise value of year {Present_year} ?\n"))
Present_year_minus_one_Enterprise_value = float(input(f"Enterpise value of year {Present_year-1} ?\n"))
Present_year_minus_two_Enterprise_value = float(input(f"Enterpise value of year {Present_year-2} ?\n"))
Present_year_minus_three_Enterprise_value = float(input(f"Enterpise value of year {Present_year-3} ?\n"))
Present_year_minus_four_Enterprise_value = float(input(f"Enterpise value of year {Present_year-4} ?\n"))

# Taking values of EV/EBITDA of past years 
Present_year_EV_by_EBITDA = float(input(f"EV/EBITDA of year {Present_year} ?\n"))
Present_year_minus_one_EV_by_EBITDA = float(input(f"EV/EBITDA of year {Present_year-1} ?\n"))
Present_year_minus_two_EV_by_EBITDA = float(input(f"EV/EBITDA of year {Present_year-2} ?\n"))
Present_year_minus_three_EV_by_EBITDA = float(input(f"EV/EBITDA of year {Present_year-3} ?\n"))
Present_year_minus_four_EV_by_EBITDA = float(input(f"EV/EBITDA of year {Present_year-4} ?\n"))

# Taking Non Current Liability value (https://www.moneycontrol.com/financials/mindtree/balance-sheetVI/MT13)
Non_Current_Liability = float(input(f"TOTAL NON-CURRENT LIABILITIES Total Non-current Liabilities of year {Present_year}\n"))

# Taking Total numbers of shares in market (https://www.moneycontrol.com/financials/mindtree/capital-structure/MT13#MT13)
Total_numbers_of_shares = int(input(f"Total numbers of shares in market till {Present_year} ?\n"))

#Formulas ----------------------------------------------------------------------------------------------------
# Taking out EBITDA from above values
Present_year_EBITDA = float(Present_year_Enterprise_value / Present_year_EV_by_EBITDA)
Present_year_minus_one_EBITDA = float(Present_year_minus_one_Enterprise_value / Present_year_minus_one_EV_by_EBITDA)
Present_year_minus_two_EBITDA = float(Present_year_minus_two_Enterprise_value / Present_year_minus_two_EV_by_EBITDA)
Present_year_minus_three_EBITDA = float(Present_year_minus_three_Enterprise_value / Present_year_minus_three_EV_by_EBITDA)
Present_year_minus_four_EBITDA = float(Present_year_minus_four_Enterprise_value / Present_year_minus_four_EV_by_EBITDA)

# Growth in EBITDA
Growth_in_Present_year_minus_one = float((Present_year_EBITDA-Present_year_minus_one_EBITDA)/Present_year_minus_one_EBITDA*100)
Growth_in_Present_year_minus_two = float((Present_year_minus_one_EBITDA-Present_year_minus_two_EBITDA)/Present_year_minus_two_EBITDA*100)
Growth_in_Present_year_minus_three = float((Present_year_minus_two_EBITDA-Present_year_minus_three_EBITDA)/Present_year_minus_three_EBITDA*100)
Growth_in_Present_year_minus_four = float((Present_year_minus_three_EBITDA-Present_year_minus_four_EBITDA)/Present_year_minus_four_EBITDA*100)

# Making List of needed 3 years of EBITDA to get the average 3 year growth
Growth_in_EBITDA = [Growth_in_Present_year_minus_one, Growth_in_Present_year_minus_two, Growth_in_Present_year_minus_three]

# Average 3 Year growth in EBITDA
Average_3_Year_growth_in_EBITDA = float(sum(Growth_in_EBITDA)/3)

# Expected EBITDA 
Expected_EBITDA = float((Present_year_EBITDA * (Average_3_Year_growth_in_EBITDA + 100)) / 100)

# Forcasted Value of Enterprise Value 
Forcasted_Value = Expected_EBITDA * Present_year_EV_by_EBITDA - Non_Current_Liability

# Shares Outstanding till present year divided by crores
Share_outstanding = float(Total_numbers_of_shares / 10000000)

# Calculating Target Price
Target_price = Forcasted_Value/Share_outstanding

# Calculating Entry Price
Entry_price = Target_price * 0.75

#OUTPUT ----------------------------------------------------------------------------------------------------
print(f"The Entry price for the stock we analysis is {Entry_price}")
print(f"The target price for the stock we analysis is {Target_price}")
print(f"Overall estimated profit generated is {Target_price-Entry_price} in {Present_year}")