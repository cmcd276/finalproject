#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import xlsxwriter
import os 

def greet_user():
    print("Enter the name of a file directory: ")
    some_directory = input() #storing typed-in prompt as a variable
    print("Thank you. One moment.")
    return some_directory #passing off whatever answer the previous lines have given

def initial_read(basepath):
    #basepath = some_directory
    allthepaths = []
    for entry in os.listdir(basepath):
        otherpath = os.path.join(basepath, entry)
        if os.path.isdir(otherpath):
            initial_read(otherpath)
        else:
            print(otherpath)
        allthepaths.append(otherpath)
    return allthepaths
        
             


        
returned_directory = greet_user() #telling the computer that it's time to do this task and storing the output of that task into a variable

roughlist = initial_read(returned_directory)

print(roughlist)


# In[ ]:


name = returned_directory + '\inventorylist.xlsx'

print(name)


workbook = xlsxwriter.Workbook(name)
worksheet = workbook.add_worksheet()
row = 0
col = 0

for filename in roughlist:
    split_filename = filename.split("\\")
    print(split_filename)
    for piece in split_filename:
        worksheet.write(row, col, piece)
        col+=1
    row +=1
    col =0
workbook.close()


# In[ ]:




