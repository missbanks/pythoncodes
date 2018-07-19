
                            #TASK - 1

'''     Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5
        between 2000 and 3200 (both included).
        the numbers obtained should be printed in a comma - seperated sequence on  a single line
'''

# if num % 5 == 0 and num % 7 !=0:

# for i in range (2000,3201):
#     if (i % 7 == 0 and i % 5 !=0):
#         print (i, end=',')

                    #TASK - 2
'''     Write a program which can compute the sum of a given numbers,
        The results should be printed in a comma - seperated sequence on a single line 
        Suppose the following input is supplied to the program
        4
        Then, the output should be 
        10
'''

# user_input = 4
# for i in range(0, user_input):
#     user_input += i
#     print(i, user_input)
# print(user_input)

                #TASK - 3
'''     Write a program which can compute the factorial of a given numbers.
        The results should be printed in a comma- seperated on a single.
        Suppose the following input is supplied to the program:
        8
        Then, the output should be:
        40320
'''

# user_input = 8
# for i in range(1, user_input):
#     user_input *= i
#     # print (i, user_input)
# print(user_input)


            # TOPIC: WhileLoop
#WhileLooop syntax
# while a is something:
#     # do some stuff
# else:
#     # do this stuff
#
#                       #TASK - 1
# list_of_departments = ['physics','maths','computer science',linguistics']
# list_of_numbers = [1,2,3,4,5,6,7, 'figure','alpha']

# user_dept = input("Enter your departments:"):
#         while user dept in list_of_departments and user_age in the list of ages

                        #Example
# i = 0
# while i <= 10: #exit condition
#     # print("i is now {}".format(i))
#     i += 1


                    #TASK -2
''' use a while loop to print out the first ten multiples of 5'''
# i = 1
# while i <=10:
#     # print(i*5)
#     print("{} times 5 == {}".format(i, i*5))
#     i += 1

#TASK -3
'''use a while loop to print mutiples of 2 and factores of 5 between 0 and 50
'''
# i = 1
# while i <=50:
#     print(i % 2 == 0) and (i % 5 == 0)
#     i += 1

    #TASK
available_exits = ["east", "north", "west", "south"]
list_of_ints =


# available_exits = ["east", "north", "west", "south"]
# chosen_exit =""
# count = 0
# while chosen_exit not in available_exits:
#     if count == 3:
#         print("Sorry your time is up")
#         break
#     chosen_exit = input ("Please choose a direction:")
#     count += 1
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
# else:
#     print("aren't you glad you got out of there!")

#TASK
number = 2
while number >0:
    number = int(input("Enter a number:"))
    for i in range(1,number):
        number *=i
    print(number)
else:
    print("you did not enter a valid number")

#TASK (0 is not regarded as a valid integer)
# number_1 = 0
# number_2 = 1
# if number_2:
#     print(True)
# else:
#     print(False)


                ##ASSIGNMENT
                #Guessing Game

'''     Get the user to select any valid integer
        Check if the number is equal to your set number
        If the user input is lower ask him to guess higher
        Else ask him to guess lower
        The user has only five tries 
        If the user guesses the '''