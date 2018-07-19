# list is defined as a homogenous group of items although
# in practise homogenity is not actually enforced

# to create
list_1 = []
list_2 = list()

#to create a list of string and add items to it
list_1.append("egg")
list_1.append("spam")
list_1.append("milk")
list_1.append("bacon")
list_1.append("cheese")
list_1.append("butter")

list_1 = ['eggs', 'spam', 'milk', 'bacon', 'cheese', 'butter']
# print(f"{list_1[0]} is an ingredient for baking")
# print(list_1.index("eggs"))

# list are mutable
list_1[4] = "peanut butter"
del list_1[4]
# print(list_1)

# To check if an item is in a list

# if "butter" in list_1:
    # print(list_1.index("butter"))
# else:
    # print("butters is not in the list")

# for item in list_1:
# if 'butter' in list_1:
#         print(True)
# else:
#         print(False)
# list_1.sort() #arranges the list in alphabetical order
# print(list_1)

list_of_ints = [6,8,4,2,5]
list_of_ints.reverse()
# print(list_of_ints)
# print(len(list_1)) #to get the lenght of a list
# print(list_1[0]) #to get an item in a list
# print(list_1.index('spam')) #to get the position of an item in a list
#for item in list_1:
    # print(item)
    # print('The item position is {} and the item name is {}'.format(list_1.index(item), item))

list_2.append(2)
list_2.append(4)
list_2.append(6)
list_2.append(8)
list_2.append(10)
list_2 = [2, 4, 6, 8, 10]

""" challenge
    create a list of ten books you know, sort them in their correct order 
     loop through the books and print the book name and index"""

list_of_books = ["king", "queen", "spade", "heart", "hero", "diamond", "grace", "faith", "charity", "hope"]
list_of_books.sort()

#print(list_of_books)

# for item in list_of_books:
    # print('The item position is {} and the item name is {}'.format(list_of_books.index(item), item))
    # print(f"{list_of_books.index(item)} is an item for {item}")

list_3 = list(range(1,10,2)) #print odd numbers
list_4 = list(range(2,10,2)) #print even numbers

# print(list_3)
# print(list_4)

numbers = list_4 + list_3
numbers.sort()#arranges the list in ascending order
# print(numbers)

#list comparisms
# if list_2 == list_3:
#     print(True)
# else:
#     print(False)
#
# if list_2 > list_4:
#     print(True)
# else:
#     print(False)

tens =list() #List of numbers that are multiples of seven
eights =[] #List of numbers that are multiples of 8
fives =[]

first_100_numbers = range(1,101)
print(first_100_numbers)
# for num in first_100_numbers:
#     if num % 10 == 0:
#         tens.append(num)
#     continue
# for num in first_100_numbers:
#     if num % 8  == 0:
#         eights.append(num)
#     continue
# for num in first_100_numbers:
#     if num % 5 == 0:
#         fives.append(num)
#     continue

# print(common_elements)

print(tens)
print(eights)
print(fives)

common_elements= []
# for number in eights:
#     if number in tens and number in fives:
#         common_elements.append(number)
#     else:
#         continue

# print(common_elements)

menu = [
         ['egg','butter','bacon'],
         ['egg','cheese','bacon','beef'],
         ['egg','spam','spam','bacon'],
         ['egg','spam','spam','spam','bacon','cheese'],
         ['egg','spam'],
         ['egg','egg','bacon','cheese']
       ]

# print(len(menu))
# print(menu[1])

# for i in menu[2]:
#     print(i)

# for spam in menu:
#     if spam in spam:
#         print(i)



# print(menu[1][1])

#to print out all the items in the third list
# for meal in menu:
    # print(meal)

# print(meal[2])
# for meal in menu:
#     if 'spam' in meal:
#         continue
#     else:
#         print(meal)
#     for ingredients in meal:
#         print(ingredients)

# menu = [
#         [], [], [], [], [], []
#         ]

                            #challenge
# create a list of all even nnumbers from 2-50
# create a list of all odd numbers from 1-50
# iterate through the list of even numbers and find their sum
# iterate through the list of odd numbers and find their sum
#(HINT: do research on the internet for this)
# from the menu list above write a program to print out list without "bacon"

# even_numbers = []
# odd_numbers = []
even_numbers = list(range(2,51,2))
odd_numbers = list(range(1,51,2))

add_all_even_numbers = 0
add_all_odd_numbers = 0

for num in even_numbers:
    add_all_even_numbers += num
    print(' {} plus {}'.format(num, add_all_even_numbers))
    add_all_even_numbers += num
    print('egual {}'.format(add_all_even_numbers))
    print('=='*10)

for num in odd_numbers:
    print(' {} plus {}'.format(num, add_all_odd_numbers))
    add_all_odd_numbers += num
    print('egual {}'.format(add_all_odd_numbers))
    print('=='*10)


numbers = range(1,51)
# print(numbers)

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 2 ==1:
        odd_numbers.append(num)
    else:
        continue

# print(even_numbers)
# print(odd_numbers)