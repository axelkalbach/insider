from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
url = "http://openinsider.com/"
driver.get(url)

sales = driver.find_element_by_xpath('/html/body/div[2]/div[4]/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[1]/td[1]/input[2]')
sales.click()

min_dollar = driver.find_element_by_xpath('/html/body/div[2]/div[4]/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[3]/td[2]/input[1]')
min_dollar.send_keys('250')

min_own_per = driver.find_element_by_xpath('/html/body/div[2]/div[4]/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td/fieldset/table/tbody/tr[4]/td[2]/input[1]')
min_own_per.send_keys('10')

sort_by_trade_date = driver.find_element_by_xpath('/html/body/div[2]/div[4]/form/table/tbody/tr/td[4]/table[2]/tbody/tr[1]/td[2]/select/option[2]')
sort_by_trade_date.click()

max_results = driver.find_element_by_xpath('/html/body/div[2]/div[4]/form/table/tbody/tr/td[4]/table[2]/tbody/tr[2]/td[2]/input')
max_results.clear()
max_results.send_keys('100')

search_btn = driver.find_element_by_xpath('/html/body/div[2]/div[4]/form/table/tbody/tr/td[4]/table[2]/tbody/tr[4]/td[2]/input')
search_btn.click()

table_data = []

for i in range(1, 101):
    print(i)
    table_data.append([])
    for j in range(1, 14):
        data = driver.find_element_by_xpath(f'/html/body/div[2]/table/tbody/tr[{i}]/td[{j}]')
        table_data[i - 1].append(data.text)

df = pd.DataFrame(
        table_data,
        columns=['X', 'Filing Date', 'Trade Date', 'Ticker', 'Company Name', 'Insider Name', 'Title', 'Trade Type', 'Price', 'Quantity', 'Owned', 'Ownership Change', 'Value']
    )

df.to_csv('Insider.csv', index=False)

print(table_data)