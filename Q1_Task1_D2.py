#Extract the ‘text’ in all the CSV files and store them into a single ‘.txt file’.
#Chaper5_Fundamentals of python pp118
#ensure default set to plain text
#writing text to file 'r' input 'w' output 

#talks to the computers operating system to access and manipulate the files
import os
#imports functions and tools to manipulate csv files
import csv

#set directory name to locate the output text file (use / to avoid conflict) 
# Do we store these on github to make is executable for all of us?
input_csv = "E:/chuditchwerkroom/2024_Werkroom/0000_CDU/2024_CDU/2024 SEM 2/HIT137/Working_Python Files/Assignment 2_HIT137_CAS_080/Q1_CSV files"

#set directory name to locate the output text file (use / to avoid conflict) 
#Do we store these on github to make is executable for all of us?
output_txt ="E:/chuditchwerkroom/2024_Werkroom/0000_CDU/2024_CDU/2024 SEM 2/HIT137/Working_Python Files/Assignment 2_HIT137_CAS_080/Q1_file_output/HIT137_A2_Q1.1.txt"

#open the output_txt to bring in csv
with open(output_txt, 'w') as outputfile:
    #loop the csv files (textbook pg65 Looping processes)
    for filename in os.listdir(input_csv):
        #filter out unwanted file types
        if filename.endswith('.csv'):
            #read all the various csv files as one filepath
            file_path = os.path.join(input_csv, filename)
            #open and read csv data (pp120) and (https://realpython.com/python-csv/)
            with open(file_path,'r') as csvfile:
                reader = csv.reader(csvfile)
                #draw in filename from each file to separate data sets from each file!!!!!!!!!!!may not need to keep
                outputfile.write(f"__________ Why the flick wont this work: {filename} __________\n")
                #convert the information to strings comibining rows and separating by(, )
                for row in reader:               
                   outputfile.write(', '.join(row) + '\n')
                   #you all know I had to fill in this time with something interesting in the terminal!
                   print('THERE IS A LOT OF DATA TO PROCESS')
                   print('THERE                            ')
                   print('      IS A LOT OF DATA           ')
                   print('Arrrrrrrrrrrrhhhhhhhhh!!!')
                   print('                       TO PROCESS')
                   print('THERE IS A LOT OF DATA TO PROCESS')
                   print('                                    Sorry this is approximately 101 SECONDS of you life you will not get back...')
                   print('                                                    You almost have time to brush your teeth')
                   print('Please Wait Impatiently')
                   print('                                                           Do NOT neglect your gums!')
                   print('Wait')
                   print('Patiently...')
                   print('YOU GOT TO BELIEVE IN THE POWER OF YOUR PROCESSOR')
                   print('or')
                   print('IMPATIENTLY!!!!!!')
                   print('Depending on your particular personality quirks.')
                   #add in running man or interesting loop for terminal viewing fun I am not taking this out NO WAY maybe a countdown.
                   #measure runtime pp391
print('THANKYOU, Your text has been extracted you can now access HIT137_A2_Q1.1 in notepad')
#----------------------------------------------------------------------------------------------------------------------------------------------------
#My main issue with this so far is how do I do the directory in a general way?? Do we store the input output on github?
#I havent watched todays github tutorial so maybe that will say how????


#-----------------------------------------------------------------------------------------------------------------------------------------------------
