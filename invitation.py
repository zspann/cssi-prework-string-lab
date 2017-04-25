
### Challenge 1 - Percy Replacement:
def percy_replacer(string_about_percy):
    return string_about_percy.replace("Percy", "Ron")

### Challenge 2 - String Interpolation:
def weasley_invitation(name,day,date,month):
    return "The family of {first_name} Weasley proudly invite you to celebrate their graduation from Hogwarts on {day} the {date} of {month}. Festivities will be held at The Burrow. See you then!".format(first_name = name, day = day, date = date, month = month)

### Challenge 3 - Seating Location
def seating_location(last_name):
    location = "middle section."
    if last_name[:1] == "A":
        location = "rear section."
    elif last_name[:1] == "B":
        location = "rear section."
    elif last_name[:1] == "C":
        location = "rear section."
    elif last_name[:1] == "D":
        location = "rear section."
    elif last_name[:1] == "E":
        location = "rear section."
    elif last_name[:1] == "F":
        location = "rear section."
    elif last_name[:1] == "G":
        location = "rear section."
    elif last_name[:1] == "W":
        location = "front row."
    return "You have a reserved seat in the {seat}".format(seat = location)

###Challenge 4 - All Together
### Passing only one of the two tests - not sure why?
def create_invitation(first_name, last_name, message):
    print "DEAR " + first_name.upper() + ",\n" + message + "\nP.S. " + seating_location(last_name)
