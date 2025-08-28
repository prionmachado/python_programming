def main():
    with open("File/Problems/alice.txt","r",encoding="utf-8-sig") as f:
        contents = f.readlines()
    
    chapter1 = contents[53:263] 

    with open("File/Problems/chapter1.txt","w",encoding="utf-8-sig") as f:
        f.writelines(chapter1) 

main() 