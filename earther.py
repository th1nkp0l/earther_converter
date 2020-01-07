#!/usr/bin/python3

from datetime import date

'''
Earther Converter is a program designed to take a user's input and do some age
conversions based on what planet they're from.
If from Earth, takes user's birth date and calculates their age first.
If from another planet, takes user's age in {planet} years as the starting point.

Goals:
Uses conversion table from csv to do all the math
Learn to work with dates in python3
Do some web scraping for relevant info. For now, all will come from csv.
Create a "spellcheck" that deals with the month inputs.
    If user input is not in any of the accepted month lists, run it through
    the fixer. Checks for mismatched order of letters or missing letters.
    Obviously could just limit the user by implementing a drop down type menu,
    but this is an opportunity to build something interesting.
'''

# TO DO
# Create a function for the count to three, then quit, functionality. Is there
# a way to do this given that one of my questions will require a for loop and
# others will not?

# defines some options when asked a yes or no question
affirmative = ["yes", "y", "ye", "yea", "affirmative", "yep", "yeah", "1", "affirm"]
negative = ["no", "n", "nope", "nah", "negative", "0", "neg"]

# defines some options that the user might input when asked their birth month
month_dict = {
"01" : ["january", "jan", "jan.", "1", "01", "ja"],
"02" : ["february", "feb", "feb.", "2", "02", "f", "fe"],
"03" : ["march", "mar", "mar.", "3", "03", "marc"],
"04" : ["april", "apr", "apr.", "4", "04", "apri"],
"05" : ["may", "5", "05"],
"06" : ["june", "jun", "jun.", "6", "06"],
"07" : ["july", "jul", "jul.", "7", "07"],
"08" : ["august", "aug", "aug.", "8", "08", "au"],
"09" : ["september", "sept", "sept.", "9", "09", "se", "septe", "septem"],
"10" : ["october", "oct", "oct.", "10", "10", "octo", "octob"],
"11" : ["november", "nov", "nov.", "11", "11", "nove", "novem"],
"12" : ["december", "dec", "dec.", "12", "12", "dece", "decem", "decemb"]
}

days_in_month = {
"01" : 31,
"02" : 29,
"03" : 31,
"04" : 30,
"05" : 31,
"06" : 30,
"07" : 31,
"08" : 31,
"09" : 30,
"10" : 31,
"11" : 30,
"12" : 31
}

# function for determining user's Earth birth date
def earth_birth():
    print("An Earther, ke? Ha!")
    birth_year = input("What year ya born? \n>>> ")
# while loop gives the user 3 tries to input a permitted value
# sets initial value as unknown for the while loop to work within
    count = 0
    while count < 3:
        count += 1
        month_input = input("What month ya born? \n>>> ").lower()
# for loop and if statement test for presence of user input in the dictionary
# of possible months. If found, sets month variable to the key value, which is
# month in %m or zero-padded decimal format
        for i in month_dict:
            if month_input in month_dict[i]:
                birth_month = i
                count = 4
                break
    if count == 3:
        quit()
    count = 0
    while count < 3:
        count += 1
        birth_day = int(input("And what day? \n>>> "))
        if birth_day in range((days_in_month[birth_month])+1):
            count = 4
    if count == 3:
        quit()
    return birth_year, birth_month, birth_day

# defines a function to calculate user's age based on birth date input
def earth_age_calc(birth_year, birth_month, birth_day):
    today = date.today()
    month_print = (month_dict[birth_month])[0].capitalize()
    print(f"Born on Earth, {month_print} {birth_day}, {birth_year}.")
    print(f"Today is {today}")
    print("I guess that makes you SOME years old.")

terran = input("You an Earther? \n>>> ")

if terran.lower() in affirmative:
    year, month, day = earth_birth()
    earth_age_calc(year, month, day)
elif terran.lower() in negative:
    print("Then where ARE you from? >>>")
else:
    print("You don't follow instructions too well, eh?")
