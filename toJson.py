import json
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

dict1 = {}
 
# fields in the sample file 
fields =['name', 'eng_desc', 'de_desc', 'hit_mod', 'dmg_mod', 'hit_type']
file= open(file_path)
l=0
for line in file:
        
    # reading line by line from the text file
    description = list( line.strip().split(';', 6))
    
    # for output see below
    print(description)       
    # loop variable
    i = 0   
    # intermediate dictionary
    dict2 = {}
    while i<len(fields):
         
            # creating dictionary for each employee
            dict2[fields[i]]= description[i]
            i+=1
    dict1[description[0]]=dict2
    l+=1
 
# creating json file        
out_file = open("size.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()