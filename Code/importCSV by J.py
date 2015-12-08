# import CSV file


# import csv 
import csv

# read csv file
ifile  = open("input.csv","r")

# reader module to read csv file
read = csv.reader(ifile)



# save data into myList
myList = []
for i in read:
    myList.append(i)

# now elements in myList are also list which includes every variables.

myList.remove(myList[0])

# remove the variable name (first column in the excel file)

# We only need the time to identify the call's category
# say connection time is 4/6/2015 10:23:25
# we only need the "10"
# so I create the following func.

def getconnectiontime(islist):

    a = islist[3]
    if len(a) == 11:
        return a[7]
    else:
        return a[7:9]

# this can also be constructed under a class as a method

for i in myList:
    b = int( getconnectiontime(i))
    if 7 <= b < 15:
        print('it was a day-time called')
    elif 15 <= b < 23:
        print('it was a evening called')
    else:
        print('it was a night called')


# this is just a demo for how we use the above fumc
# we can delete it afterward

