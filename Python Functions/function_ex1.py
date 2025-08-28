def print_Len(list):
    print(len(list))

num_list = [10,20,30,40,70]
hero = ["ironman","spiderman","thor"]

print_Len(num_list)  # Output: 5 
print_Len(hero)  # Output: 3


def print_list(list):
    for i in list:
        print(i,end=" ")

print_list(hero) 
# Output: ironman spiderman thor 