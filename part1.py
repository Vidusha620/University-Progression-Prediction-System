#Part 1
#Specify the valid credits
valid_credits=[0, 20, 40, 60, 80, 100, 120]
progress_count,trailer_count,retriever_count,exclude_count = 0, 0, 0, 0
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
 elif pass_credits == 120:
          print("Progress")
          progress_count+=1
 elif pass_credits == 100:
          print("Progress(module trailer)")
          trailer_count+=1
 else:
          print("Do not Progress-module retriever")
          retriever_count+=1

 #Quit or continue
 x=str(input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: "))
 if x=="q":
     break
 elif x=="y":
     continue    

#Histogram
print("Histogram")
print(f"Exclude {exclude_count} : ", end="")
print("*" * exclude_count)
print(f"Progress {progress_count} : ", end="")
print("*" * progress_count)
print(f"Trailer {trailer_count} : ", end="")
print("*" * trailer_count)
print(f"Retriever {retriever_count} : ", end="")
print("*" * retriever_count)

#Outcome in total
outcome=exclude_count+progress_count+trailer_count+retriever_count
print(outcome,"outcomes in total.")
