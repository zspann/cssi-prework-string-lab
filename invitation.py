import re #this allows regular expressions

### Challenge 1 - String Interpolation:
def weasley_invitation(name,day,date,month):
    return "The family of {first} Weasley proudly invite you to celebrate their graduation from Hogwarts on {day_of_week} the {date_of_month} of {month}. Festivities will be held at The Burrow. See you then!".format(first=name,day_of_week=day,date_of_month=date,month=month)


### Challenge 2 - The Guest List
#The function should return the first initial and last name of each guest.

def invitee_name(full_name):
    if len(full_name.split())==2:
        name=full_name.split()[0][0] + ". " + full_name.split()[1]
    else:
        name=full_name.split()[0][0] + ". " + full_name.split()[2]
    return name


###Challenge 3 - All Together
def create_invitation(name, message):
    return name.upper() + ",\n" + message

print create_invitation(invitee_name("Alstor 'Mad-Eye' Moody"), weasley_invitation("Ron","Sunday", "May", "18th" ))
