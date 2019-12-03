#!/usr/bin/env python
# coding: utf-8

# python final-project-claire.py
# follow instructions in prompt
# excel sheet saved one directory up ../

import xlsxwriter
import os

def greet_user():
    print("Enter the name of a file directory: ")
    some_directory = input() #storing typed-in prompt as a variable
    print("Thank you. One moment.")
    return some_directory #passing off whatever answer the previous lines have given
allthepaths = []
def initial_read(basepath):

    for entry in os.listdir(basepath):
        otherpath = os.path.join(basepath, entry)
        if os.path.isdir(otherpath):
            initial_read(otherpath)
            allthepaths.append(otherpath)
        else:
            print(otherpath)
        allthepaths.append(otherpath)
    return allthepaths





returned_directory = greet_user() #telling the computer that it's time to do this task and storing the output of that task into a variable

roughlist = initial_read(returned_directory)




print("\n Please provide a simple nickname for your inventory file. No need to provide filetype. Example: mydirectory")
identifier = input()
name = returned_directory + '../inventorylist'+identifier+'.xlsx'



workbook = xlsxwriter.Workbook(name)
worksheet = workbook.add_worksheet()
row = 0
col = 0

print("Are you a Windows (W) User? Or Mac (M) User?")
os = input()
print("Great! The inventory excel sheet is located in "+ name)
for filename in roughlist:
    #print(filename)
    if os =="W":
        split_filename = filename.split("\\")
    elif os =="M":
        split_filename = filename.split("/")
    else:
        print("You didn't input a W or an M, please try the program again.")
    #print(split_filename)
    for piece in split_filename:
        worksheet.write(row, col, piece)
        col+=1
    row +=1
    col =0
workbook.close()



# In[ ]:
