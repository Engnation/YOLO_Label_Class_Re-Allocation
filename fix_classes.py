#! /usr/bin/env python3

#This script reads YOLO label text files and replaces specified class label #s
#Author: Ryan Schmalenberg

import glob, os

#Input directory of label text files that need classes to be re-assigned
label_txts =(glob.glob("Test_Labels_Needing_Fixing/*.txt")) 
fixed_label_txt_path = "Fixed_Label_TXTs" #Output directory

    # Function to convert  
def listtostring(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

def writetofile(txt,data):
    f = open(txt, "w")
    f.write(data)
    f.close()

def appendtofile(txt,data):
    f = open(txt, "a")
    f.write(data)
    f.close()

def inspect(var): 
    print(f"Name: {var.__repr__} | type: {type(var)} | value: {var}") 


if __name__ == "__main__":

    for txt in label_txts:

        #Separate file name from directory
        filename = txt.split("/")[1]
    
        #Specify output directory
        fixed_label_txts = os.path.join(fixed_label_txt_path,filename)

        with open(txt, "r") as f_read:

            count = 0

            for line in f_read.readlines():

                inspect(line)
                
                f_contents = f_read.read()

                line_list = list(line)

                #Enter classes you want to replace here:
                #ToDo (iterate this for n# of classes)
                if line_list[0] == '0':
                    line_list[0] = '8'
                elif line_list[0] == '1':
                    line_list[0] = '3'

                data = listtostring(line_list)
                
                inspect(data)

                if count == 0:
                    writetofile(fixed_label_txts,data)
                if count > 0:
                    appendtofile(fixed_label_txts,data)

                count += 1

        f_read.close()        

    print("done!")

