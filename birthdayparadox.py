import datetime, random

def getBirthdays(numberOfBirthdays):
    # This returns a list of number random date objects for birthdays
    birthdays = []

    for i in range(numberOfBirthdays):
        # Note that the year is unimportant as the program assumes all these birthdays are on the same year
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    # this function returns the date of a birthday that occurs more than once in the birthdays list
    if len(birthdays) == len(set(birthdays)):
        return None # If all the birthdays are unique, return none
    
    # This code compares each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # returns the matching birthday