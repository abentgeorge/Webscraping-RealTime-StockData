# Credits - eMaster Class Academy


import requests
from bs4 import BeautifulSoup

url = ('https://finance.yahoo.com/quote/0001.HK?p=0001.HK&.tsrc=fin-srch')

 # CK Hutchison Holdings Limited

# STEP 1 - IDENTIFICATION OF CLASS/SPAN ID HOLDING VALUE

r = requests.get(url)
print(r.text)

web_content = BeautifulSoup(r.text, 'lxml')
web_content = web_content.find('div', class_= 'My(6px) Pos(r) smartphone_Mt(6px)') 

# Inspect url or Check Image 1 and 2 in Repository 

# .find('type of object', attributes)

# TO PASS MORE THAN ONE ATTRIBUTE, NEED TO CONVERT ATTRIBUTES INTO A DICTIONARY 
# IE USE {} 
#--------------------------
web_content = web_content.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'})
print(web_content)

web_content = BeautifulSoup(r.text, 'lxml')
web_content = web_content.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'})
print(web_content)
#-------------------------------

# THE DATA WE NEED IS IN THE SPAN<> CLASS (THE 54.950)
# IE <span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="32">54.950</span>
# NEED ANOTHER FIND TO GET THE OBJECT BUT USE A .TEXT TO GET THE EXACT STOCK VALUE

web_content = BeautifulSoup(r.text, 'lxml')
web_content = web_content.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'})
web_content = web_content.find('span').text
print(web_content)

# STEP 2 -  PLACE THE WHOLE CODE INTO A FUNCTION TO CALL WHENEVER

def real_time_price(stock_code):  
    url = ('https://finance.yahoo.com/quote/') + stock_code +\
                ('.HK?p=') + stock_code + ('.HK&.tsrc=fin-srch')
                
    # ORIGINAL URL ='https://finance.yahoo.com/quote/0001.HK?p=0001.HK&.tsrc=fin-srch'
                
    # edit the URL so you can manually enter stuff later on
                
    # '/' used at eol to continue code on next line python
    
    r = requests.get(url)
    web_content = BeautifulSoup(r.text, 'lxml')
    web_content = web_content.find('div', {"class" : 'My(6px) Pos(r) smartphone_Mt(6px)'})
    web_content = web_content.find('span').text
    
    # TO PREVENT PULLING A NULL VALUE DURING A DATA UPDATE 
    
    if web_content ==[]:
        web_content = '9999' # ie if you see 9999 you know you pulled during an update
    
    return(web_content)

# TEST FUNCTION
web_content = real_time_price('0001') # 0001 = stock code
print(web_content)

# STEP 3 - CREATE A LOOP TO PULL DATA AND PLACE INTO CSV



# LOOP TO KEEP PULLING DATA  | PLACE DATA IN CSV

import pandas as pd
import datetime       #timestamp to know at what time we pulled the data

#   Create a list that contains codes you want to monitor

HSI = ['0001', '0002', '0003', '0005']

for step in range(1,101): 

#range() function returns a sequence of numbers, 
#starting from 0 by default, and increments by 1 (by default),stops before a specified 



    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    
    #TO TRACK MORE THAN ONE PRICE CODE NEED ANOTHER FOR LOOP
    
    for stock_code in HSI:
         price.append(real_time_price(stock_code)) # Place function 
         
        # in price, time stamp in other col
    col = [time_stamp]
    col.extend(price)   # .extend adds items to the end of an iterable list
    
    df = pd.DataFrame(col) # data frame to store the column result
    df = df.T   #pandas.DataFrame.T property is used to transpose index 
    #          and columns of the data frame ie make rows
    df.to_csv('rt-stockdata.csv', mode = 'a', header = False)  # save to csv, mode = append, no headers
    
    print(col)
    
