import csv

# tuples is defined as a heterogenous group of items although
# in practiise heterogenity is not actually enforced

#to create a tuple
tuple_1 = () # tuple literal
tuple_2 = tuple() # tuple method

#tuple are imutable
# print(tuple_1)
# print(tuple_2)
#
# flightsfile = oepn("fights.csv")
# reader = csv.reader(flightsFile)
# for item in reader:
#     origin, destination, duration = item
#     print

tuple_3 = (
         ("olamide","who you epp",2016),
         ("tiwa savage","badd",2014),
         ("davido","fia",2017),
         ("kiss daniel","no do",2018)
          )

# name, title, year = ("olamide", "badoo",2016) #unpacking
# print(name)
# print(year)

for item in tuple_3:
    print(item)
    name, title, year = item
    print(f"Artist: {name}, song title: {title}, year: {year}")
# print(tuple_3[1])

# for item in tuple_3:(item)
#     print


