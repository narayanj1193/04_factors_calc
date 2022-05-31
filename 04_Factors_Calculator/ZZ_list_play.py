# set up a list...

my_list = []

# generate 4 random numbers between 1 & 10...
for item in range(0,4):

        # generate random number between 1 and 10
        random_num = random.randint(1, 10)

        # add number to list 
        my_list.append(random_num)


# print the *unsorted* list...
print(my_list)

# sort the list
my_list.sort()

my_list_len = len(my_list)

# print the sorted list
print()
print(my-list)
print('The list has {} items".format(my_list_len))')
print()