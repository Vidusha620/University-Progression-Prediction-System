#Part 2
#Specify the valid credits
valid_credits=[0, 20, 40, 60, 80, 100, 120]
progress_count,trailer_count,retriever_count,exclude_count = 0, 0, 0, 0
progress_list,trailer_list,retriever_list,exclude_list = [], [], [], []
x=0
while x!="q":
 try:  

    #Prompt the user for credit inputs
    pass_credits = int(input("Enter your credits at pass: "))
    if pass_credits not in valid_credits:
        print("Out of range.")
    else:
       defer_credits = int(input("Enter your credits at defer: "))
       fail_credits = int(input("Enter your credits at fail: "))
 except ValueError:
    print("Interger required.")

 #Calculate the total credits
 total_credits = pass_credits + defer_credits + fail_credits

 #Display the appropriate progression outcome
 if total_credits != 120:
        print("Total Incorrect")    
 elif fail_credits >= 80:
        print("Exclude")
        exclude_count+=1
        exclude_list.append([pass_credits, defer_credits, fail_credits])
 elif pass_credits == 120:
        print("Progress")
        progress_count+=1
        progress_list.append([pass_credits, defer_credits, fail_credits])
 elif pass_credits == 100:
        print("Progress(module trailer)")
        trailer_count+=1
        trailer_list.append([pass_credits, defer_credits, fail_credits])
 else:
        print("Do not Progress-module retriever")
        retriever_count+=1
        retriever_list.append([pass_credits, defer_credits, fail_credits])

 #Quit or continue
 x=str(input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: "))
 if x=="q":
     break
     

#Print the list
print("Part 2: ")

for item in progress_list:
    print(f"Progress - {', '.join(str(i) for i in item)}")
for item in trailer_list:
    print(f"Progress (module trailer) - {', '.join(str(i) for i in item)}")
for item in exclude_list:
    print(f"Exclude - {', '.join(str(i) for i in item)}")
for item in retriever_list:
    print(f"Module retriever - {', '.join(str(i) for i in item)}")

#Part 3
#Text file

with open("output.txt", "w") as newfile:
    newfile.write("Part 3: \n")
    for item in progress_list:
        newfile.write(f"Progress - {', '.join(str(i) for i in item)}\n")
    for item in trailer_list:
        newfile.write(f"Progress (module trailer) - {', '.join(str(i) for i in item)}\n")
    for item in exclude_list:
        newfile.write(f"Exclude - {', '.join(str(i) for i in item)}\n")
    for item in retriever_list:
        newfile.write(f"Module retriever - {', '.join(str(i) for i in item)}\n")
        



    
    
