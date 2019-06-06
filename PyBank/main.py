
# coding: utf-8

# In[62]:


# HW instructions:
# https://github.com/the-Coding-Boot-Camp-at-UT/UTAMCB201904DATA3/tree/master/03-Python/Homework/Instructions


# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# 
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# 
# The total number of months included in the dataset
# 
# The net total amount of "Profit/Losses" over the entire period
# 
# The average of the changes in "Profit/Losses" over the entire period
# 
# The greatest increase in profits (date and amount) over the entire period
# 
# The greatest decrease in losses (date and amount) over the entire period
# 
# As an example, your analysis should look similar to the one below:
# 
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# In[63]:


import pandas as pd
import numpy as np
import csv


# In[64]:


url = "https://raw.githubusercontent.com/marazap90/python-challenge/master/PyBank/budget_data.csv"
df = pd.read_csv(url)
df.head(10)


# In[65]:


# The total number of months included in the dataset
tm = df["Date"].count()
tm


# In[66]:


# The net total amount of "Profit/Losses" over the entire period
tp = df["Profit/Losses"].sum()
tp


# In[67]:


# The average of the changes in "Profit/Losses" over the entire period
ac = df["Profit/Losses"].mean()
ac


# In[68]:


# The greatest increase in profits (date and amount) over the entire period
gp = df["Profit/Losses"].max()
gp


# In[69]:


# The greatest decrease in profits (date and amount) over the entire period
gl = df["Profit/Losses"].min()
gl


# In[70]:



print("FINANCIAL ANALYSIS")
print("==================")
print("")

print("Total Months: " + str(tm))
print("Total: $" + str(tp))
print("Average Change: $" + str(ac))
print("Greatest Increase in Profits: $" + str(gp))
print("Greatest Decrease in Profits: $" + str(gl))


# In[71]:


f = open("output.txt", "a")

print("FINANCIAL ANALYSIS", file=f)
print("==================", file=f)
print("", file=f)

print("Total Months: " + str(tm), file=f)
print("Total: $" + str(tp), file=f)
print("Average Change: $" + str(ac), file=f)
print("Greatest Increase in Profits: $" + str(gp), file=f)
print("Greatest Decrease in Profits: $" + str(gl), file=f)


f.close()

