#!/usr/bin/python3

from datetime import date
from datetime import datetime

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

#A dictionary of this system's planets and any nicknames
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
        else:
            if x == 0:
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
        print("Try again.")
    print("\tWas a simple question, sabakawala!")
    quit()

# function for determining user's Earth birth date
def earth_birth():
    print("Ok Tumang. Let's find out how old you are.")
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
        else:
            if x == 0:
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
        age = earth_age
    print("Belter taps his head as he works through some math...")
    input("Press RETURN/ENTER to get his attention.")
    print("Belter: Give me a break, I was doing a little math! \n")
    return age


#Add a quick calculation
    return choice

print("***You're with an belter who you've never met in a dark store room.***\n")

print("Belter: \"So you need travel docs. \n\
\tKowlting gonya gut - eveything gon' be good. \n\
\tNow let's get this done before we get caught, kopeng.")
full_name = input("\tKeting nem to? I mean, what's your full name?\" \nYou: ")
names = full_name.split(" ")
first_name = names.pop(0)
last_name = names.pop(-1)

print(f"Belter: \"Are you an Earther, beratna?\"")
terran = input(f"{first_name}: ")
if terran.lower() in affirmative:
    birth_planet = "Earth"
    print("Belter: \"What planet you going to, Earther?\"")
    destination = planet_checker()
    year, month, day = earth_birth()
    earth_age = earth_age_calc(year, month, day)

elif terran.lower() in negative:
    print("Belter: \"Then where are you from?\"")
    birth_planet = planet_checker()
    print(f"Belter: \"What planet you going to, {birth_planet} kopeng?\"")
    destination = planet_checker()
    earth_age = "null"

else:
    print(f"You don't follow instructions too well, eh {first_name}?")

age = planet_age_calc(birth_planet, earth_age, destination)

print(f"Belter: \"OK Mr. {last_name}, we're finished here. \n\
\tHere are the docs, beratna. You're now officially from {destination}. \n\
\tJust don't tell me what you're doing with these.\n\
\tAlways watch out for doors and corners. That's where they get you.\"\n")
print("***You look down at your newly minted docs.*** \n")

input(">>>Diplomatic Travel Authorization<<< ")

print(f"Citizen: {first_name} {last_name}")
print(f"Birth Planet: {destination}")
print(f"Age: {age} DEMONYM years")
print(f"Approved Destinations: {birth_planet}")
