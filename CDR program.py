#   This is a program to analyze Call Detail Record
#   
#
#
#
import matplotlib.pyplot as plt
from CDRLib import *

# Input CSV data
print("Questo è un programma per l'analisi dei CDR")
print("Il file deve essere nominato in input.csv")
name = "input.csv"  # a demonstration CSV file

# Use a customized readCSV function to read CSV file
myList = readCSV(name)

# Using a helper func to recall a class "call()"  
data=[makecall(i) for i in myList]  

# Analysis options
print("Ci sono quattro analisi disponibili\n")
print("A: Il numero e la percentuale di ERRORI di rete")
print("B: Il numero e la percentuale di ERRORI per timezone")
print("C: La somma di chiamate per timezone")
print("D: Durata delle chiamate e costi in giornate differenti\n")
# Decision for User
end = "y"
while end =="y":
    ans = input("Please choose one: (A/B/C/D)?")
    if ans == "A":
        networkERR(data)
    elif ans == "B":
        networkERRbyzone(data)
    elif ans == "C":
        call_by_time(data)
    elif ans == "D":
        call_by_day(data)
        
    end=input("\n keep analyzing (y/n): ")
print("Grazie~")
        
        



























