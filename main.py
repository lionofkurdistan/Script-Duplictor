import shutil

def print_equal():
  print("=" * 30)


print("Welcom To Script Duplictor By Lion Of Kurdistan ")

source = str(input("Please Enter Youer Suorce Paht: "))

targets_times = int(input("How Many Targets Do You Have? "))

paths = [ ]

for time in range(targets_times):
  time = str(input("Enter Target path: "))
  paths.append(time)
  
for path in paths:
  shutil.copy2(source, path)
  print("Done")
  
print_equal()
print("Successfull")
print_equal()
input("Prees Enter To Close...")