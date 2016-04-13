import re #this allows regular expressions

### Challenge 1 - Percy Replacement:
def percy_replacer(string_about_percy):
    return string_about_percy.replace("Percy","Ron")

### Challenge 2 - String Interpolation:
def weasley_invitation(name,day,date,month):
    return "The family of {first} Weasley proudly invite you to celebrate their graduation from Hogwarts on {day_of_week} the {date_of_month} of {month}. Festivities will be held at The Burrow. See you then!".format(first=name,day_of_week=day,date_of_month=date,month=month)


### Challenge 3 - Seating Location

def seating_location(last_name):
  if last_name[0] == "W":
    return "You have a reserved seat in the front row."
  elif last_name[0] <= "G":
    return "You have a reserved seat in the rear section."
  else:
    return "You have a reserved seat in the middle section."


###Challenge 4 - All Together
def create_invitation(first_name, last_name, message):
  return "DEAR {},\n{}\nP.S. {}".format(first_name.upper(),message,seating_location(last_name))
