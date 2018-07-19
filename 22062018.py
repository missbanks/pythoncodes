
# ASSIGNMENT
# current_time = "friday 2pm"
# add_time = 51
# convert_to_days = 51 // 24
# remainder_hours = 51 % 24
#
# print(convert_to_days,"days")
# print(remainder_hours,"hours")
#
# time_to_go_off = 2 + remainder_hours
# print(time_to_go_off)

# current_time_in_am = 2
# # time_to_wait_in_hours = 11
# # if current_time_in_am:
# #     if time_to_wait_in_hours < 10:
# #         alarm_go_off_time = current_time_in_pm_or_am + time_to_wait_in_hours
# #         print(alarm_go_off_time,"am")
# #     else:
# #         alarm_go_off_time = current_time_in_pm_or_am + time_to_wait_in_hours
# #         print(alarm_go_off_time,"pm")
# #     else:
# #
# #     alarm_go_off_time = current_time_in_pm_or_am = alarm_go_off_time
# #     print
# #
# # alarm_go_off_time = current_time + time_to_wait


                        ### TOPIC :
#  Forloops, While loops, augmented assignments, break, continue, switch
#
#        FORLOOPS
# for i in range(0,10):
# #     print(i, end=',')
#
# for i in range(0,10,2):
#         print(i, end=',')

                    #CLASS WORK
    # print the squares of multiples of 3 between 0 and 30
# for i in range(0, 31, 3):
#     print (int(i)**2, end=',')

# for i in range (30,0,-1):
#     print(i, end=',')

    # print the first hundred numbers in reverse order (0-100)
# for i in range (100,-1,-1):
#         print(i, end=',')

# numbers = "9,222,543,876,9786,567"
# for char in numbers:
#     if char in"0123456789":
#         print(char, end='')
#     else:
#         continue

# numbers = "9,222,543,876,9786,567"
# for char in numbers:
#     if char in"0123456789":
#         print(char, end='')
#     else:
#         break

# numbers = "9,222,543, 876,9786,567"
# for char in numbers:
#     if char == "," or char == ' ':
#         continue
#     if int(char) % 2 ==1:
#         print(char)
#     else:
#         continue

                #CLASS TASK
#Get a user to enter any calendar year. If it is a leap year
#display text "this is a leap year" else "this is not a leap year"
#leap year:
# """divisible by 4, not divisible by 100"""

# input = ("leap year % 4")
# calendar_year = int(input(leap year % 4))
# ordinary_year = (divisible by 4 )
# ordinary year = 2

# calendar_year = "leap year"
#
# name = input("enter a year")
# leap_year = int(input("enter a year") % 4 == 0)
# if enter_year % 4 == 0:
#     print("not a leap year")
# if int(input(calendar_year)% 4 == 0):
#     print("leap_year")
# else:
#     print("not a leap_year")

# cal_year = int(input("enter a year: "))
# if cal_year % 4 ==0:
#     print("{} is a leap year".format(cal_year))
# else:
#     print("{} is not a leap year".format(cal_year))

                #Augmented Assignment
# even_number = 2
# # even_number +=1
# # print(even_number)
# even_number = even_number + 1
# print(even_number)

# for char in range (10):
#     char **=2
#     print(char)
# #

#
# for char in range(10):
#         chare = char **2
#         print(chare)
#
    #     num = 3
    #     num += 1
    #     num -= 2
    # num *=2
    #

#                   #mulitiplication table
# for i in range(2,13):
#     for j in range(1,13):
#         print("{0:2d} times {1:4d} is {2:4d}".format(i,j,i*j), end='\t')
#         print('')
#     print('====='*10)

    # step 1
    # first loop will take 2
    # second loop will take 1
    # second loop will take 2 .......12

    # second loop will take 3
    # second loop will take 1
    # second loop will take 2 .......12


    ###TASK
    #4. Print the multiplication table of the first ten odd numbers

# for i in range(16):
#     if int(i) % 2 ==1:
#         for j in range(1,13):
#             print("{0:2d} times {1:4d} is {2:4d}".format(i,j,i*j), end='\t')
#             print('')
#         print('====='*10)
#
# for i in range(1,16,2):
#     for j in range(1,13):
#         print("{0:2d} times {1:4d} is {2:4d}".format(i,j,i*j), end='\t')
#         print('')
#     print('====='*10)
#
# for i in range(1,16):
#     if int(i) % 2 ==1:
#         for j in range(1,13):
#             print("{0:2d} times {1:4d} is {2:4d}".format(i,j,i*j), end='\t')
#             print('')
#         print('====='*10)
#     else:
#         continue

        ## TOPIC:WHILE LOOP

number = 0
while number <10:
    print("The number is {}".format(number))
    number += 1



