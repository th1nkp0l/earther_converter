#!/usr/bin/python3

from datetime import date
from datetime import datetime
import pandas as pd

'''
Earther Converter is a program designed to take some user input and do age
conversions based on what planet they're from.
If from Earth, takes user's birth date and calculates their age first.
If from another planet, takes user's age in home planet years as the
starting point.

Goals:
Uses conversion table from csv to do all the math
Learn to work with dates in python3
Do some web scraping for relevant info. For now, all will come from csv.
Create a some checks to ensure good inputs for:
    year, month, day, planet, yes, no
'''

# TO DO
# Create a function for the count to three, then quit, functionality. Is there
# a way to do this given that one of my questions will require a for loop and
# others will not?

# defines some options when asked a yes or no question
affirmative = [
"yes", "y", "ye", "yea", "aye", "affirmative", "yep", "yup", "yeah", "1", "affirm"
]
negative = [
"no", "n", "nope", "nah", "nay", "negative", "0", "neg"
]

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

#Sets possibilities for days of the month
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

planets = [
"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune",
"Pluto"
]

#Evaluates for proper birth years
def birth_yr_input():
    now = datetime.now()
    tuple = now.timetuple()
    print(f"Belter: \"What year ya born, bosmang?\"")
    for x in range(0,3):
        choice = input(f"{first_name}: ")
        if choice.isdigit() and int(choice) <= tuple[0]:
            birth_year = int(choice)
            return birth_year
        elif x == 0:
            print("Belter: \"Try again. What's your birth year?\"")
        elif x == 1:
            print("Belter: \"We don't have much time! Give me the year.\"")
        else:
            print("Belter: \"I'm not going to jail today! Pashang fong!\"")
            quit()

def birth_mth_input():
#Gives the user 3 tries to input a permitted value
    print("What month ya born?")
    for x in range(0,3):
        choice = input(f"{first_name}: ").lower()
#For loop and if statement tests for presence of user input in the dictionary
#of possible months. If found, sets month variable to the key value, which is
#month in %m or zero-padded decimal format
        for i in month_dict:
            if choice in month_dict[i]:
                birth_month = i
                return birth_month
        if x == 0:
            print("Belter: \"Try again!\"")
        elif x == 1:
            print("Belter: \"That's not an Earth month!\"")
        else:
            print("Belter: \"I don't have time for you, nekangepensa!\"")
    quit()

def birth_day_input(birth_month):
    print("Belter: \"And what day\"")
    for x in range(0,3):
        choice = int(input(f"{first_name}: "))
        if choice in range((days_in_month[birth_month])+1):
            return choice
        elif x == 0:
            print("Belter: \"That doesn't make sense, try again.\"")
        elif x == 1:
            print("Belter: \"I'm getting tired of your mistakes.\"")
        else:
            print("\tWas a simple question, sabakawala! Get out of here!")
            quit()

# function for determining user's Earth birth date
def earth_birth():
    print("Belter: \"Ok Tumang. Let's find out how old you are.\"")
    birth_year = birth_yr_input()
    birth_month = birth_mth_input()
    birth_day = birth_day_input(birth_month)
    return birth_year, birth_month, birth_day

def planet_checker():
    for x in range(0,3):
        choice = input(f"{first_name}: ")
        choice = choice.capitalize()
        if choice in planets:
            return choice
        elif x == 0:
            print("Belter: That's not a planet in this system.")
        elif x == 1:
            print("Belter: Man, come on and give me an answer!")
        else:
            print("\tSabaka! I don't have time for this. Pashang fong!")
            quit()


#Defines a function to calculate user's Earth age based on birth date input
def earth_age_calc(birth_year, birth_month, birth_day):
    today = date.today()
    month_printed = (month_dict[birth_month])[0].capitalize()
    print(f"Born on Earth, {month_printed} {birth_day}, {birth_year}.")
    print(f"The date on Earth today is {today}")
    age = 33
    print(f"That makes you {age} years old.")
    return age

#Calculates user's age in destination planet years
def planet_age_calc(birth_planet, earth_age, destination):
    if birth_planet != "Earth":
        print(f"Belter: \"How old in {birth_planet} years are you?\"")
        age = input(f"{first_name}: ")
        age *= 2
    else:
        print(f"Belter: \"Why would you want to leave Earth, anyway, {first_name}?\n \
        Nevermind, don't tell me!\"")
        age = earth_age
    print("Belter taps his head as he works through some math...")
    input("...")
    input("... ...")
    print("Belter: Give me a break, I was doing a little math! \n")
    return age

#Questioning path for users born on Earth
def earth_born():
    birth_planet = "Earth"
    demo_birth = demonym_izer(birth_planet)
    print("Belter: \"What planet you going to, Earther?\"")
    destination = planet_checker()
    demo_destination = demonym_izer(destination)
    year, month, day = earth_birth()
    earth_age = earth_age_calc(year, month, day)
    return birth_planet, destination, earth_age, demo_destination, demo_birth

#Questioning path for users born off Earth
def elsewhere_born():
    print("Belter: \"Then where are you from?\"")
    birth_planet = planet_checker()
    demo_birth = demonym_izer(birth_planet)
    print(f"Belter: \"What planet you going to, {demo_birth} kopeng?\"")
    destination = planet_checker()
    demo_destination = demonym_izer(destination)
    earth_age = "null"
    return birth_planet, destination, earth_age, demo_destination, demo_birth

def demonym_izer(origin):
    demonym = (data.loc[data.planet == origin, 'demonym'])
    demonym = (demonym.to_string(index = False)).strip()
    return demonym

#Add a quick calculation
    return choice

data = pd.read_csv("conversiontable.csv")

print("***You're with an belter who you've never met in a dark store room.***\n")

print("Belter: \"So you need some travel docs? \n\
\tKowlting gonya gut - eveything gon' be good. \n\
\tNow let's get this done before we get caught, kopeng.")
full_name = input("\tKeting nem to? I mean, what's your full name?\" \nYou: ")
full_name = full_name.title()
names = full_name.split(" ")
first_name = names[0]
last_name = names[-1]

print(f"Belter: \"Are you an Earther, beratna?\"")

for count in range(0,3):
    terran = input(f"{first_name}: ")
    if terran.lower() in affirmative:
        birth_planet, destination, earth_age, demo_destination, demo_birth = earth_born()
        break
    elif terran.lower() in negative:
        birth_planet, destination, earth_age, demo_destination, demo_birth = elsewhere_born()
        break
    elif count == 0:
        print(f"You don't follow instructions too well, eh {first_name}?")
    elif count == 1:
        print(f"You don't follow instructions too well, eh {first_name}?")
    else:
        print(f"Oh fuck off, then.")
        quit()

age = planet_age_calc(birth_planet, earth_age, destination)

print(f"Belter: \"OK Mr. {last_name}, we're finished here. \n\
\tHere are the files, beratna. You can now call yourself a {demo_destination}. \n\
\tJust don't tell me what you're doing with these.\n\
\tAlways watch out for doors and corners. That's where they get you.\"\n")
print("***You look down at your hand terminal.*** \n")

input(">>>Diplomatic Travel Authorization<<<\n")

#Create list of all planets other than the new birth planet to use in app dest
#planet_list = 

print(f"\tCitizen: {full_name}")
print(f"\tBirth Planet: {destination}")
print(f"\tAge: {age} {destination} years")
print(f"\tApproved Destinations: ")
