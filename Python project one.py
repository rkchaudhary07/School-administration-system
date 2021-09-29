#Project1
import csv
def write_into_csv(info_list):
  with open("student_info.csv","a",newline=" ") as csv_file:
    writer = csv.writer(csv_file)
    if csv_file.tell() == 0:
      writer.writerow(["Name", "Age", "Contact", "E-mail"])
    writer.writerow(info_list)

condition = True
while(condition):
  student_info = input("Enter student data in following format: (Name, Age, Contact, E-mail): ")
  print("Enter information: " . student_info)

  student_info_list = student_info.split(" ")
  print("Entered split info is " . str(student_info_list))

  write_into_csv(student_info_list)

  condition_check = input("Enter (yes/no) if wanna enter another syudent info")
  if condition_check == "yes":
    condition = True
  elif condition_check == "no":
    condition = False