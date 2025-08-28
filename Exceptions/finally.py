try:
    l = [1,2,3,4,5,5,6] 
    i = int(input("Enter the index :"))
    print(l[i]) 
except:
    print("Index out of range") 
finally:
    print("This block will always execute") 