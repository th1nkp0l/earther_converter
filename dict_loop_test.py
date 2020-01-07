#!/usr/bin/python3

dict = {
"01" : ["january", "jan", "jan.", "1", "01"],
"02" : ["february", "feb", "feb.", "2", "02"],
"03" : ["march", "mar", "mar.", "3", "03"],
"04" : ["april", "apr", "apr.", "4", "04"],
"05" : ["may", "5", "05"],
"06" : ["june", "jun", "jun.", "6", "06"],
"07" : ["july", "jul", "jul.", "7", "07"],
"08" : ["august", "aug", "aug.", "8", "08"],
"09" : ["september", "sept", "sept.", "9", "09"],
"10" : ["october", "oct", "oct.", "10", "10"],
"11" : ["november", "nov", "nov.", "11", "11"],
"12" : ["december", "dec", "dec.", "12", "12"]
}

month = "oct."
test = "0"

for i in dict:
    if month in dict[i]:
        print(i)
        test = i
        break
    else:
        print("succs to succ")

print(test)
