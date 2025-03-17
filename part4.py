#Part 4
#Valid credits
valid_credits=[0, 20, 40, 60, 80, 100, 120]
progress_count,trailer_count,retriever_count,exclude_count = 0, 0, 0, 0
progress_list,trailer_list,retriever_list,exclude_list = [], [], [], []
dictionary = {}
x=0
while x!="q":
    
 try:
     #Prompt the user for their University of Westminister student id
     UoW_number = input("Enter your UoW number: ")

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
        dictionary[UoW_number] = f"Exclude - {pass_credits}, {defer_credits}, {fail_credits}"
 elif pass_credits == 120:
        print("Progress")
        progress_count+=1
        progress_list.append([pass_credits, defer_credits, fail_credits])
        dictionary[UoW_number] = f"Progress - {pass_credits}, {defer_credits}, {fail_credits}"
 elif pass_credits == 100:
        print("Progress(module trailer)")
        trailer_count+=1
        trailer_list.append([pass_credits, defer_credits, fail_credits])
        dictionary[UoW_number] = f"Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}"
 else:
        print("Do not Progress-module retriever")
        retriever_count+=1
        retriever_list.append([pass_credits, defer_credits, fail_credits])
        dictionary[UoW_number] = f"Do not progress (module retriever) - {pass_credits}, {defer_credits}, {fail_credits}"

 #Quit or continue
 x=str(input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: "))
 if x=="q":
     break

#Print dictionary
for i,j in dictionary.items():
    print(f"{i} : {j}", end=" ")
print()
