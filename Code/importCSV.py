# import CSV file


# import csv 
import csv

# read csv file
ifile  = open("input.csv","r")

# reader module to read csv file
read = csv.reader(ifile)

# save data into myList
myList = []
for row in read:
    for i in row:
        myList.append(i)

# transfer List into myStr
myStr = "+".join(myList)


print(myStr[0:200])
print(myList[0:20])

    
