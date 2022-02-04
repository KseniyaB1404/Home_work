my_list = [14, 700, 155, 19, 22, 66, 185, 165, 75, 99]
for i in my_list:
    if i > 100:
     print(i)

#####################################################################################

my_list = [140, 70, 15, 190, 220, 660, 18, 16, 75, 990]
my_results = []
for i in my_list:
    if i > 100:
        my_results.append(i)
for i in my_results:
    print(i)

#####################################################################################

my_list = [12,22,55,84,61,8]
my_list_1 = my_list[-1] + my_list[-2]
new_my_list = my_list.copy()
new_my_list.append(my_list_1)
print(new_my_list)

#####################################################################################

my_string = '0123456789'
my_list = []

for i in my_string:
    for j in my_string:
        my_list.append(int(f'{i}{j}'))
        print(my_list)

