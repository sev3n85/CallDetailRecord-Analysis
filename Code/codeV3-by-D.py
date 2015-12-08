# import CSV file


# import csv 
import csv

# read csv file
ifile  = open("inputsmall.csv","r")

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
#Dare's comment: We can also implement a counter here for our histogram graph
#I'm looking into creating an output file for each of the connection time so that we can analyze them seperately

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



'''Create a class for calculation '''
#
#This is a method used to get the call failure reson 
#
def finishreason(alist):
    return alist[6]

#set the counter
NR = 0
B = 0
NE = 0
HU = 0


for b in myList:
    c = str( finishreason(b))
    #print(c)
    if c == 'NOT_REACHED':
        NR = NR + 1
    elif c == 'BUSY':
        B = B + 1
    elif c == 'NETWORK_ERROR':
        NE = NE + 1
    else:
        HU = HU + 1
print("###################################################################################")
print("From this entire list we have", NR, "- Not Reached call reason", B, "Busy call reason", HU, "Hangup call reason", NE, "Network Error call reason")
    
