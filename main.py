print(f"*****************Lets Start*********************\n") 
print("      Deviyon aur Sajjano, chaliye milkar khelte hai Kaun Banega Crorepati\n")
questions = [
  ["Which of the following is an exit controlled loop?", "while loop", "for loop", "do-while","none of the above", "None", 4],
  ["What is the size of the int data type (in bytes) in C?", "1", "2", "8","4", "None", 4],
  ["If p is an integer pointer with a value 1000, then what will the value of p + 5 be?", "1200", "1025", "1005","1020", "None", 4],
  ["Which of the following are not standard header files in C?", "conio.h", "stdlib.h","stdio.h","none of the above", "None", 4],
["In which of the following languages is function overloading not possible?", "Python", "Java", "C","C++", "None", 4],
["Which of the following function is used to open a file in C++?", "fgets", "fopen", "fclose","fseek", "None", 4],
[" Which of the following are correct file opening modes in C?", "r", "w", "rb","All of the above", "None", 4],
["What is the return type of the fopen() function in C?", "Pointer to a file object", "An integer", "Pointer to a integer","An string", "None", 4],
["Which of the following is not a storage class specifier in C?", "Static", "Typedef", "Extern","Volatile", "None", 4],

["Which of the following will occur if we call the free() function on a NULL pointer?", "Compiletime error", "Runtime error", "Undefined behaviour","The program will execute normally", "None", 4],
]

levels = [1000, 5000, 10000, 25000, 50000, 100000, 500000, 2000000, 5000000,1000000]
answer=[3,4,4,4,3,2,4,3,4,4]
money = 0
for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}\n")
  print("#", question[0])
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}         d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  print("\n\nComputer jii iss jawab ko lock kiya jaye")
  if(reply == answer[i]):
      print("Bilkul sahi jawab")
      print(f"Correct answer, you have won Rs. {levels[i]}")
      if(i<9):
          print("Agla prashn aapke computer screen par ye rha!!!!")
      if(i == 9):
       money=10000000 
       print("You are Genius")
       print(f"Your take home money is {money}")
       break;      
  elif(i>=3 and i<=7):
      money = 10000
      print("Wrong answer!")
      break
  elif(i>7 and i<=9):
      money = 5000000
      print("Wrong answer!")
      break
  else:
    print("Wrong answer!")
    break 

if(money!=10000000):
  print(f"Your take home money is {money}")
  
print(f"***************Go to your home****************             ") 
