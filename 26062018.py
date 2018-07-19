
                            #TASK
'''
    Get user to enter a letter of the alpahabet
    check if it is a vowel or consonant
    if it is a vowel display message using string format saying 'This letter is a vowel'
    if not display a message using string format also saying 'This is not a vowel'
'''


#TEST

#1. get user input
# user_input = (input('Please enter a letter')).lower()
# vowels_of_alpha = 'aeiou'
# if user_input in vowels_of_alpha:
#     print("This {} is a vowel".format(user_input))
# else:
#     print("This {} is not a vowel".format(user_input))

'''
    get the user to enter a number 
    check of the number is a multiple of 3 and factor of 5
    if it is print out the square of the number 
    else print out this number is not a factor of three and multiple of 5 
    Test values: 15, 9, w, 12
    15 should be true and square should be 225
    9 should be false
    w should be false 
    12 should be false 
'''

# user_input = int(input ('Please enter a number'))
#     if(user_input % 3 == 0 and user_input % 5 == 0):
#         print ("The square of {} and {}".format(user_input, user_input **2))
#
#     else:
#         print (" This is not a factor if three and multiple of 5")

                    #TASK
'''
    Small_alphabets = "abcdefghijklmnopqrstuvwxyz"
    your objective is to iterate through small_aphabets
    and covert each to a capital letter using uper() method
    print out small_alphabets
'''
# user_input = (input('Please enter a letter'))
# small_alpahbets = 'abcdefghijklmnopqrstuvwxyz'
# for char in small_alpahbets:
#         print(char.upper())


                #TASK
'''
    your task is to loop through the first 50 even numbers and 
    check if a number is a multiple of 4 print it else continue
    '''
# for i in range(2,51,2):
#     # print(i)
#     if i % 4 ==0:
#     print(i)
# else:
#     continue

        #TASK
'''     
        Get the user to enter his or her IP address
        An IP address consist of 4 numbers, seperated from each other with a full stop.
        but your program should just count however many munbers are in the IP address entered 
        and print it
        Test values of the input you may use are:
        
        192.168.0.1
        10.0.123456.255
        172.16.55.28
        127.0.0.1
'''

# old_string = 'pieces of paper'
# new_string = ''
# for char in old_string:
#     if char == ' ':
#         continue
#     else:
#         new_string += char
#
# print(new_string)

# old_string = "172.16.55.28"
# new_string = ''
# for char in old_string:
#     if char == '.':
#         continue
#     else:
#         new_string += char
# print(new_string)
#
# print(len(new_string))
#
# Ip_address = (input("Please type your IP address"))
# print(len(new_string))
# #
# Example -2
#
# old_string = "172.16.55.28"
# new_string = ''
# for char in old_string:
#     if char == '.':
#         continue
#     else:
#           new_string += char
#print(new_string)
#
#  print(len(new_string))
# #
#Ip_address = (input("Please type your IP address"))
#print(len(new_string))

                #TASK
'''     create  range of values between 0 and 100
        check if the number meets the following criteria
        1.prime number 
        then build a string of the prime numbers between 0 and 100 inclusive 
'''

# user_number = int(input("Please type a number"))
# status = True
# if user_number < 2:
#     print("This is not a prime number")
#     status = False
# else:
#     for i in range(2, user_number):
#         if user_number % i == 0:
#             status = False
#     if status:
#         print("This is a prime number")
#     else:
#         print("This is not a prime number")



user_number = int(input("Please enter a number"))
for i in range(2,user_number):
    if user_number % i == 0:
        print("This is not a prime number")
        break

    else:
        print("This is a prime number")
        break

#     # if i == 1:
#     #     print ("{} is a prime number".format)
#     # elif i ==2:
#
#     if (i % i == 1 and i % i == 0):
#         print(i)


