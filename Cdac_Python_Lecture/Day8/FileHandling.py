# File Handling
# It is the handling of creeation ,opening,reading and writing and closing files.
# Purpose:store the data permanently
# RAM --> Disk
# --Need:
''' 
Ex: Student data, Employee,Records,logs,reports,configuration,files,data is required to store.
    Diffrent types of file:txt, csv,json,sql....


Opening File
File_object = Open("Filename","Mode")

Mode of File:
1.Read - r
Opens file for reading
File must be Existing
Default Mode
Ex:
    f = open("abc.txt","t")
    print(f.read())
    f.close()

2.Write - w
-Open file for Writing
Create file if it doesnot Exist.
If file already exist,old content is erased.

f = open("abc.txt","w")
f.write("Hello Cdac Mumbai")
f.clost()
3.Append - a
Opem file for appending
Create file if it does not exist
New Data is added at the end of file
Ex: 

4. Exclusive Create Mode:
    Create a new file
    If File is already exsist it will give errors

Binary Mode: NON Text File
Images pdf,audio,Vedio,etc
-'b' is added in the mode
-'r':rb,   w: wb,   a:ab

Combined File Mode:
    -Read : r+
    -Read and Write File must exist
    Pointers Starts at the bedining of 1st Character

    -Write: w+
    -Read and Writes
    -Overwrite existing  content
    Creates file if it is not existing


-Append:a+
        -Read and Append
        -Creates file if not exist
      
        -Writing always happens at the end of files

File Pointer/Cursor Position:
1. tell(): return current Position
2. seek(): moves pointer to a specific posistion

        
        
        '''


f = open("Day8/abc.txt","r")
print(f.read())
f.close()

f = open("Day8/abc.txt","w")
f.write("Hello Cdac Mumbai")
f.close()



f = open("Day8/abc.txt","a")
f.write(f"\n Are you Getting It !!")
f.close()


f= open("Day8/abcd.txt","x")
f.write("\nImplementation is neccessary ")
f.close()


f = open("Day8/abc.txt","r")
data = f.read()
print(data)
f.close()