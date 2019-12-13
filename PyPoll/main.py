import os, csv

PyPall_csv = os.path.join("C:\Course work\python-challenge\PyPoll\Resources\election_data.csv")
Pypall_txt = os.path.join("C:\Course work\python-challenge\PyPoll\Pypall.txt")

Vote_dic = {}
Total_Vote = 0
Voter_Name_List = []
Voter_percenage_List = []
Voter_Total_list = []
i,j,Count = 0,0,0
Vote_dic = {"Voter_ID":[], "County": [], "Candidate": []}

with open(PyPall_csv, newline="", encoding="UTF-8") as csv_file:
    Vote_reader = csv.reader(csv_file, delimiter=',')
    VOte_header = next(csv_file)
    for row in Vote_reader:
        Total_Vote += 1
        Vote_dic["Voter_ID"].append(row[0])
        Vote_dic["County"].append(row[1])
        Vote_dic["Candidate"].append(row[2])
        
    for item in Vote_dic["Candidate"]:   
        if item not in Voter_Name_List:
            Voter_Name_List.append(item)

    for i in range(len(Voter_Name_List)):
        for line in Vote_dic["Candidate"]:
            if Voter_Name_List[i] in line:
                Count += 1
        Voter_Total_list.append(Count)
        Count = 0
    
    for j in range(len(Voter_Total_list)):
        A = (Voter_Total_list[j]/Total_Vote)*100
        Voter_percenage_List.append(round(A,2))

    Winner = max(Voter_Total_list)
    indexx = Voter_Total_list.index(Winner)

    with open(Pypall_txt, 'w' , newline="", encoding="UTF-8") as txt_file:
        txt_file.write("Election Results")
        txt_file.write("\n----------------------------")
        txt_file.write("\nTotal Votes: %d" %Total_Vote)
        txt_file.write("\n----------------------------\n")
        for i in range(len(Voter_Name_List)):
            txt_file.write(str(Voter_Name_List[i]))
            txt_file.write("       ")
            txt_file.write(str(Voter_percenage_List[i]))
            txt_file.write("      ")
            txt_file.write(str(Voter_Total_list[i]))
            txt_file.write("\n")
        txt_file.write("----------------------------\n")
        txt_file.write("Winner:  ")  
        txt_file.write(str(Voter_Name_List[indexx]))     

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {Total_Vote}")
    print("----------------------------")
    for i in range(len(Voter_Name_List)):
        print(f"{Voter_Name_List[i]}:\t\t\t{Voter_percenage_List[i]}%  ({Voter_Total_list[i]})")
    print("----------------------------")
    print(f"Winner: {Voter_Name_List[indexx]}")