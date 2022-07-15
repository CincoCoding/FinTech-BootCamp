## @TODO: From the pathlib library, import the main class Path
#from pathlib import Path
## @TODO: Check the current directory where the Python program is executing from
#print(f"Current working directory: {Path.cwd()}")
#
## @TODO: Set the path using Pathlib
#filepath = Path("C:/Users/range/Documents/FinTech BootCamp/Class_6_Activities/08-Stu_File_IO/Unsolved/file.txt")
#
##read the file
#with open(filepath, "r") as file:
#    text = file.read()
#    print(text)
#
##Write to a different file
#    line_num = 1
#    for line in file:
#    print(f"line {line_num}: {line}")
#    line_num += 1
#    
#output_path = Path("output.txt")
#
#with open(output_path, "w") as file:
#    file.write("This is an output file. \n")
#    file.write(text)
#
from pathlib import Path

print(f'Current working directory: {Path.cwd()}')



filepath = Path('C:/Users/range/Documents/FinTech BootCamp/Class_6_Activities/08-Stu_File_IO/Unsolved/file.txt')

with open(filepath, 'r') as file:
    text = file.read()
    print(text)
    
    line_num = 1
    for line in file:
        print(f"line {line_num}: {line}")
        line_num += 1

        
output_path = Path("C:/Users/range/Documents/FinTech BootCamp/Class_6_Activities/08-Stu_File_IO/Unsolved/output.txt")


with open(output_path, 'w') as file:
    file.write("This is an output file.\n")
    file.write(text)