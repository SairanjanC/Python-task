keys=input("enter keys separeted by space: ").split()
num_list=int(input("enter the number of values in lists: "))
r_dict={}
for i in range(num_list):
    val=input(f"enter values of keys {keys[i]}: ").split()
    r_dict[keys[i]] =val
print(r_dict)
