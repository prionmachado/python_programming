with open("File/f.txt","r") as file:
    print(type(file)) 

    #Move to the 9th byte in the file
    file.seek(9) 

    #read the next 7 bytes
    print(file.read(7)) 

    #tell() returns the current position of the file 
    print(file.tell())  

with open("File/f2.txt","w") as file:
    file.write("Hello World") 

    #truncate() if you want the file to be of specific size
    file.truncate(5) 

with open("File/f2.txt","r") as file:
    #read the file
    print(file.read()) 

    #tell() returns the current position of the file 
    print(file.tell()) 