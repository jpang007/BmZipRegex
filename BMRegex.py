#ReadME 
#This script should help with adjusting a file of numbers over to a string where each number is seperated by a |
#If the numbers come in as a DOCX, it's easier to first change the file to a CSV
#Change the pathname of the file to the place on your local computer where the files lives on line 11 
#To run the code open up Terminal application on a Mac
#use the command "cd"" to enter the file location on your browser the command "ls" will help you know where you are
#Use the command python3 BMRegex.py when you are in the same directory as the file
import tkinter as tk
from tkinter import filedialog
import sys
import re
import csv
import os


zipList = []
newList = []


def UploadAction(event=None):
	filename = filedialog.askopenfilename()
	print('Selected:', filename +' to convert')
	with open(filename, mode ='r')as file: 
		# displaying the contents of the CSV file
		csvFile = csv.reader(file)

		for lines in csvFile:
			zipList.append(lines)
		for i in zipList:
			newList.append(''.join(i))
		# print (newList)
		output_string = "|".join(str(num) for num in newList)

	desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
	outputFilename = os.path.join(desktop_path, 'outputNumbers.txt')

	with open(outputFilename, "w") as file:
		file.write(output_string)
	print ("Finished output as outputNumber.txt, it should be avaliable on your desktop!")
	sys.exit()


root = tk.Tk()
l = tk.Label(root, text = "Upload a CSV file  here to convert to piped format")
l.config(font =("Courier", 14))

l.pack()
button = tk.Button(root, text='Open', width=10, height=5, font=("Helvetica", 16), command=UploadAction)
button.pack()

root.mainloop()
