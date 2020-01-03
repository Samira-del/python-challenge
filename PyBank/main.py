import os
import csv

PyBank_csv = os.path.join("Resources", "budget_data.csv")
PyBank_txt = os.path.join("PyBank.txt")
#PyBank_csv = os.path.join("C:/Course work/python-challenge/PyBank/Resources/budget_data.csv")
#PyBank_txt = os.path.join("C:/Course work/python-challenge/PyBank/PyBank.txt")

Total_months = 0
Total = 0
Total_Change = 0
profit_loses = []
date = []
Change_list = []
i,j = 0,0

with open(PyBank_csv, newline="", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    for row in csv_reader:
        profit_loses.append(int(row[1]))
        date.append(row[0])
        Total += float(row[1])
    

    for j in range(len(profit_loses)-1):
        A = profit_loses[j+1] - profit_loses[j]
        Change_list.append(A) 
        Total_Change += Change_list[j]   
    
    Average = Total_Change / len(Change_list)
    
    minval = Change_list[0]
    maxval = Change_list[0]
    for item in range(0, len(Change_list), 1):
        if Change_list[item] < minval:
            minval = Change_list[item]
            minmonth = date[i+1]
        if Change_list[item] > maxval:
            maxval = Change_list[item]
            maxmonth = date[i+1]
        i += 1
        
    
with open(PyBank_txt, 'w' , newline="", encoding="UTF-8") as txt_file:
    txt_file.write("Total Months is %d" %len(profit_loses))
    txt_file.write("\nTotal Amount of Profit and Losses is %d" %round(Total))
    txt_file.write("\nAverage Change is %d" %round(Average,2))
    txt_file.write("\nThe greatest increase in losses is ")
    txt_file.write(str(maxmonth))
    txt_file.write(str(round(float(maxval))))
    txt_file.write("\nThe greatest decrease in losses is ")
    txt_file.write(str(minmonth))
    txt_file.write(str(round(float(minval))))


print(f"Total Months is {len(profit_loses)}")
print(f"Total Amount of Profit and Losses is {round(Total)}")
print(f"Average Change is {round(Average,2)}")
print(f"The greatest increase in losses is {maxmonth} ({round(float(maxval))})")
print(f"The greatest decrease in losses is {minmonth} ({round(float(minval))})")