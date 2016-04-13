# Graduation Invitation Maker
<img src="https://s3.amazonaws.com/after-school-assets/weasley.jpg" width="150" align="left" hspace="10">
Ron Weasley is graduating from Hogwarts! He's got Percy Weasley's graduation invitations from a few years ago, which Percy wrote out by hand before sending them via owl post:

*The family of Percy Weasley proudly invite you to celebrate their graduation from Hogwarts on Saturday the 22nd of June. Festivities will be held at The Burrow. See you then!"*

Percy could have saved a lot of time by using the magic of programming to automate this task. Help Ron get these invitations printed quickly so he can spend more time playing Quidditch.

To run the tests, just type `python invitation_test.py` or `learn` into the terminal.

## Challenge 1 - Replace Percy
In `invitation.py` create a function called `percy_replacer()` that takes one parameter (a string) and returns that string with all instances of "Percy" replaced with "Ron". Hint: Look at the [.replace()](http://pythoncentral.io/pythons-string-replace-method-replacing-python-strings/) function.

```
>>>percy_replacer("Percy Weasley is Graduating!")
"Ron Weasley is Graduating"
```

## Challenge 2 - String Interpolation:
In `invitation.py` create a function `weasley_invitation()` that accepts 4 parameters, the name, the day of the week, the date and the month.  This function will use string interpolation to customize the invitation for Ron and any other future Weasleys.

```python
>>>print weasley_invitation("Ron","Sunday", "May", "18th" )
The family of Ron Weasley proudly invite you to celebrate their graduation from Hogwarts on Sunday the May of 18th. Festivities will be held at The Burrow. See you then!

```

## Challenge 3 - The Seating Location
This year, Hogwarts is being quite strict with it's seating arrangements for gradutation:
+ If the guest's last name starts with the letters A-G, they are to be seated in the "rear section"
+ If the guest's last name starts with a W, they are to be seated in the "front row".
+ All other guests may sit in the "middle section"

Write a function `seating_location()` that takes in the guest's last name and returns a string with instructions on where they are to sit during graduation.

```python
>>>print seating_location("Potter")
You have a reserved seat in the middle section.
>>>print seating_location("Weasley")
You have a reserved seat in the front row.
>>>print seating_location("Granger")
You have a reserved seat in the rear section.
```

## Challenge 3 - Putting it all Together
Most of Ron's work is done, now just write a final function, `create_invitation()` that takes three arguments, one for the guest's first name, one for the last name and one for the invitation message. The guest's first name should be complete capitalized in the salutation and followed by a comma. After a line break, the invitation's message should be printed. Finally, the seating location should be printed in the 'P.S.'

```python
>>>print create_invitation("Alistair","Moody", weasley_invitation("Ron","Sunday", "May", "18th" ))
DEAR ALISTAIR,
The family of Ron Weasley proudly invite you to celebrate their graduation from Hogwarts on Sunday the May of 18th. Festivities will be held at The Burrow. See you then!
P.S. You have a reserved seat in the middle section.
```
