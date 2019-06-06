
# coding: utf-8

# In[1]:


# HW instructions:
# https://github.com/the-Coding-Boot-Camp-at-UT/UTAMCB201904DATA3/tree/master/03-Python/Homework/Instructions


# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
# 
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# 
# The total number of votes cast
# 
# A complete list of candidates who received votes
# 
# The percentage of votes each candidate won
# 
# The total number of votes each candidate won
# 
# The winner of the election based on popular vote.
# 
# As an example, your analysis should look similar to the one below:
# 
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# In[2]:


import pandas as pd
import numpy as np
import csv


# In[3]:


url = "https://raw.githubusercontent.com/marazap90/python-challenge/master/PyPoll/election_data.csv"
df = pd.read_csv(url)
df.head(10)


# In[4]:


# The total number of votes cast

total = len(df)
total


# In[5]:


# A complete list of candidates who received votes

voted = df["Candidate"].unique()
voted


# In[6]:


# The percentage of votes each candidate won

pct = round(100*df.Candidate.value_counts()/len(df), 1)
pct


# In[7]:


# The total number of votes each candidate won

votes = df.Candidate.value_counts()
votes


# In[8]:


# The winner of the election based on popular vote.

winner = df['Candidate'].value_counts().idxmax()
winner


# In[9]:


#print summary

print("ELECTION RESULTS")
print("----------------")

print("Total Votes: " + str(total))
print("----------------")

print(list(pct.index.values)[0] + ":       " + str(pct[0]) + "%    #" + str(votes[0]))
print(list(pct.index.values)[1] + ":     " + str(pct[1]) + "%    #" + str(votes[1]))
print(list(pct.index.values)[2] + ":         " + str(pct[2]) + "%    #" + str(votes[2]))
print(list(pct.index.values)[3] + ":    " + str(pct[3]) + "%    #" + str(votes[3]))
print("----------------")

print("Winner: " + winner)
print("----------------")


# In[10]:


#write summary into the text file

f = open("output.txt", "a")

print("ELECTION RESULTS", file=f)
print("----------------", file=f)

print("Total Votes: " + str(total), file=f)
print("----------------", file=f)

print(list(pct.index.values)[0] + ":       " + str(pct[0]) + "%    #" + str(votes[0]), file=f)
print(list(pct.index.values)[1] + ":     " + str(pct[1]) + "%    #" + str(votes[1]), file=f)
print(list(pct.index.values)[2] + ":         " + str(pct[2]) + "%    #" + str(votes[2]), file=f)
print(list(pct.index.values)[3] + ":    " + str(pct[3]) + "%    #" + str(votes[3]), file=f)
print("----------------", file=f)

print("Winner: " + winner, file=f)
print("----------------", file=f)


f.close()

