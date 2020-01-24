#!/usr/bin/python3

from datetime import date
from datetime import datetime
import pandas as pd

'''
Inspired by the television show The Expanse, earther_converter is a project
built around a short interaction with a black market travel document forger.
The forger asks a series of questions to produce the eventual diplomatic
travel authorization.

Learning goals:
Uses conversion table from csv to convert one planet "age" to another.
Uses same csv to look up the demonym (Mars -> Martian) for each planet.
Work with dates in python3
Create a some checks to ensure good inputs
    year, month, day, planet, yes, no
'''

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

#lists the planets for acceptable entries
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
            print("Belter: Try again. What's your birth year?")
        elif x == 1:
            print("Belter: We don't have much time! Give me the year.")
        else:
            print("Belter: I'm not going to jail today! Pashang fong!")
            quit()

#Evaluates for acceptable birth months
def birth_mth_input():
    print("What month ya born?")
    for x in range(0,3):
        choice = input(f"{first_name}: ").lower()
#For loop and if statement tests for presence of user input in the dictionary
#of possible months. If found, sets birth_month to the key value, which is
#month in %m or zero-padded decimal format
#Will leave it as a string for later use in key lookup within dictionary
        for i in month_dict:
            if choice in month_dict[i]:
                birth_month = i
                return birth_month
        if x == 0:
            print("Belter: Try again!")
        elif x == 1:
            print("Belter: That's not an Earth month!")
        else:
            print("Belter: I don't have time for you, nekangepensa!")
    quit()

#Input and check for birth day. Only thing I decided not to do was mess with
#leap year checks. Allows 29 days in Feb.
def birth_day_input(birth_month):
    print("Belter: And what day?")
    for x in range(0,3):
        choice = input(f"{first_name}: ")
        try:
            choice = int(choice)
        except:
            print("Belter: Numbers only!")
        if choice in range((days_in_month[birth_month])+1):
            return choice
        elif x == 0:
            print("Belter: That doesn't make sense, try again.")
        elif x == 1:
            print("Belter: I'm getting tired of your mistakes.")
        else:
            print("\tWas a simple question, sabakawala! Get out of here!")
            quit()

# function for determining user's Earth birth date
def earth_birth():
    birth_year = birth_yr_input()
    birth_month = birth_mth_input()
    birth_day = birth_day_input(birth_month)
    today = date.today()
    days_in_year = 365.2425
    month_printed = (month_dict[birth_month])[0].capitalize()
    print("Belter: Ok Tumang. Let's find out how old you are.")
    print(f"Born on Earth, {month_printed} {birth_day}, {birth_year}.")
    print(f"The date on Earth today is {today}")
    birth_date = date(birth_year, int(birth_month), birth_day)
    age = int((today - birth_date).days / days_in_year)
    print(f"That makes you {age} years old.")
    return age

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

#Calculates user's age in destination planet years
def planet_age_calc(birth_planet, destination, demo_destination):
    birth_mult = (data.loc[data.planet == birth_planet, 'year_multiplier'])
    birth_mult = float(birth_mult)
    dest_mult = (data.loc[data.planet == destination, 'year_multiplier'])
    dest_mult = float(dest_mult)
    if birth_planet != "Earth":
        print(f"Belter: How old in {birth_planet} years are you?")
        for x in range(0,3):
            initial_age = input(f"{first_name}: ")
            try:
                initial_age = float(initial_age)
                break
            except:
                print("Belter: Numbers only!")
            if x == 0:
                print("Belter: That doesn't make sense, try again.")
            elif x == 1:
                print("Belter: I'm getting tired of your mistakes.")
            else:
                print("\tWas a simple question, sabakawala! Get out of here!")
                quit()
        age = initial_age / birth_mult * dest_mult
        age = round(age, 2)
    else:
        initial_age = earth_birth()
        age = initial_age / birth_mult * dest_mult
        age = round(age, 2)
    print("Belter taps his head as he works through some math...")
    input("...")
    input("... ...")
    print("Belter: Give me a break, I was doing a little math!")
    print(f"\tRemember, now you're {age} in {demo_destination} years\n")
    return age

#Questioning path for users born on Earth
def earth_born():
    birth_planet = "Earth"
    demo_birth = demonym_izer(birth_planet)
    print("Belter: \"What planet you need papers for, Earther?\"")
    destination = planet_checker()
    demo_destination = demonym_izer(destination)
    return birth_planet, destination, demo_destination, demo_birth

#Questioning path for users born off Earth
def elsewhere_born():
    print("Belter: Then where are you from?")
    birth_planet = planet_checker()
    demo_birth = demonym_izer(birth_planet)
    print(f"Belter: What's your new home planet, {demo_birth} kopeng?")
    destination = planet_checker()
    demo_destination = demonym_izer(destination)
    return birth_planet, destination, demo_destination, demo_birth

def demonym_izer(origin):
    demonym = (data.loc[data.planet == origin, 'demonym'])
    demonym = (demonym.to_string(index = False)).strip()
    return demonym

#Add a quick calculation
    return choice

data = pd.read_csv("conversiontable.csv")

print("***You're with an belter who you've never met in a dark store room.***\n")

print("Belter: So you need some travel docs? \n\
\tKowlting gonya gut - eveything gon' be good. \n\
\tNow let's get this done before we get caught, kopeng.")
full_name = input("\tKeting nem to? I mean, what's your full name? \nYou: ")
full_name = full_name.title()
names = full_name.split(" ")
first_name = names[0]
last_name = names[-1]

print(f"Belter: Are you an Earther, beratna?")

for count in range(0,3):
    terran = input(f"{first_name}: ")
    if terran.lower() in affirmative:
        birth_planet, destination, demo_destination, demo_birth = earth_born()
        break
    elif terran.lower() in negative:
        birth_planet, destination, demo_destination, demo_birth = elsewhere_born()
        break
    elif count == 0:
        print(f"Simple question, no?")
    elif count == 1:
        print(f"Let's move forward here or part ways, {first_name}.")
    else:
        print(f"OK, I'm not in the business of dealing with pendejos.")
        quit()

age = planet_age_calc(birth_planet, destination, demo_destination)

#Creates a list, then string, for approved travel destinations. All planets
#are approved by default, excluding the new home planet for obv reasons.
approved_dest = []
for p in planets:
    if p != destination:
        approved_dest.append(p)
approved_dest = ", ".join(approved_dest)


print(f"\tOK Mr. {last_name}, we're finished here. \n\
\tHere are the files, beratna. You can now call yourself a {demo_destination}. \n\
\tJust don't tell me what you're doing with these.\n\
\tAlways watch out for doors and corners. That's where they get you.\n")
input("***You look down at your hand terminal.*** \n")

print(">>>Diplomatic Travel Authorization<<<\n")

print(f"\tCitizen: {full_name}")
print(f"\tBirth Planet: {destination}")
print(f"\tAge: {age} {destination} years")
print(f"\tApproved Destinations: {approved_dest}")
