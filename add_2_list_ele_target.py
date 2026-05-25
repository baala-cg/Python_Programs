

my_list = [3, 5, 4, 3, 6, 7, 7, 2, 5]
target = 9

new_list =[]

for i in range(0, len(my_list)):
    for j in range(i+1, len(my_list)):
        if target == my_list[i] + my_list[j]:
            new_list.append(f"{my_list[i]}  and {my_list[j]}")

print(new_list)

