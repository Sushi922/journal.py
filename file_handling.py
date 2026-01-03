from datetime import datetime

def add():
  entry = input("Enter your journal entry: ")
  with open("temu.txt","a")as file:
    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write("[{}] {}\n".format(date,entry))
  print("Entry saved!")
  
def view():
  with open("temu.txt","r")as file:
    print("Your entries are:\n")
    zero = 1
    for i in file:
      print("{}.{}".format(zero,i.strip()))
      zero += 1
      
def clear():
  with open("temu.txt","w")as file:
    print("Entries have been deleted!")

def delete():
  with open("temu.txt","r")as file:
    lines=file.readlines()
  view()
  index=int(input("Which entry do you want to delete?"))
  lines.pop(index)

  with open("temu.txt","w")as file:
    for i in lines:
      file.write(i)

while True:
  print("1.Add entry")
  print("2.View entries")
  print("3.clear the entries")
  print("4.delete an entry")
  print("5.exit the app")
  
  choice=input("Please enter your choice: ")
  if choice=="1":
    add()
  
  if choice=="2":
    view()
  
  if choice=="3":
    clear()

  if choice=="4":
    delete()
    
  if choice=="5":
    print("Exiting the app")
    break
  
  else:
    print("Please enter a valid choice: ")
    