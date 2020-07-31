#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

# ifMatch function will take an excel file as input and will give output a new excel file
# It will then match the Actual PO with the PO and will give a new Column named 'Acutal Dzn'
def vlookUP(input):
    df = pd.read_excel(input)
    df1, df2 = pd.read_excel(input, sheet_name = "record"), pd.read_excel(input, sheet_name = "marks")
    df3 = pd.merge(df1,df2, on ='id', how ='inner')
    df3.to_excel("RESULT.xlsx")
    return df3
    
userInput = input("Enter the name of Excel File with Extension:")
vlookUP(userInput) 


# In[ ]:




