import sys
import os

def txt_save():
  os.system('cls')
  multiplication_table = int(input("\nEnter the multiplication table you want: "))
  last_number = int(input("Upto what number do you want it: "))
  # save_to_file = 

  filew = open(str(multiplication_table) + "x Table upto " + str(last_number) + ".txt", 'w')
  filew.write(" ")
  filew.close()

  file = open(str(multiplication_table) + "x Table upto " + str(last_number) + ".txt", 'r+')
  for iteration, x in enumerate(range(multiplication_table, last_number, multiplication_table)):
    print(str(multiplication_table) + " x " + str(iteration + 1) + " = " + str(x))
    file.write(str(multiplication_table) + " x " + str(iteration + 1) + " = " + str(x) + "\n")
  file.close()

def csv_save():
  os.system('cls')
  multiplication_table = int(input("\nEnter the multiplication table you want: "))
  last_number = int(input("Upto what number do you want it: "))
  # save_to_file = 

  filew = open(str(multiplication_table) + "x Table upto " + str(last_number) + ".csv", 'w')
  filew.write(" ")
  filew.close()

  file = open(str(multiplication_table) + "x Table upto " + str(last_number) + ".csv", 'r+')
  print(str(multiplication_table) + "," + "Multiplication Table")
  file.write(str(multiplication_table) + "," + "Multiplication Table")
  for iteration, x in enumerate(range(multiplication_table, last_number, multiplication_table)):
    print(str(iteration + 1) + "," + str(x))
    
    file.write(str(iteration + 1) + "," + str(x) + "\n")
  file.close()


if sys.argv[1] == "-txt":
  txt_save()

elif sys.argv[1] == "-csv":
	csv_save()

elif sys.argv[1] == "-t":
	txt_save()

elif sys.argv[1] == "-c":
	csv_save()

elif sys.argv[1] == "-credits":
  os.system('cls')
  print("""
███████╗███████╗ █████╗  ██████╗███████╗██████╗ 
╚══███╔╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
  ███╔╝ █████╗  ███████║██║     █████╗  ██████╔╝
 ███╔╝  ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
███████╗███████╗██║  ██║╚██████╗███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
              Made by ZeaCeR#5641
        This program uses from for loops
                  Thank You!
   """)
  
elif sys.argv[1] == "-who":
  os.system('cls')
  print("""
███████╗███████╗ █████╗  ██████╗███████╗██████╗ 
╚══███╔╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
  ███╔╝ █████╗  ███████║██║     █████╗  ██████╔╝
 ███╔╝  ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
███████╗███████╗██║  ██║╚██████╗███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
              Made by ZeaCeR#5641
        This program uses from for loops
                  Thank You!
   """)