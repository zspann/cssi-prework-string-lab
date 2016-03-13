# Graduation Invitation Maker
<img src="https://s3.amazonaws.com/after-school-assets/weasley.jpg" width="150" align="left" hspace="10">
Ron Weasley is graduating from Hogwarts! He's got Percy Weasley's graduation invitations from a few years ago, which Percy wrote out by hand before sending them via owl post.

**"The family of Percy Weasley proudly invite you to celebrate their graduation from Hogwarts on Saturday the 22nd of June. Festivities will be held at The Burrow. See you then!"**

Percy could have saved a lot of time by using the magic of programming to automate this task. Help Ron get these invitations printed quickly so he can spend more time playing Quidditch.


## Challenge 1 - String Interpolation:
In `invitation.py` create a function `weasley_invitation()` that accepts 4 parameters, the name, the day of the week, the date and the month.  This function will use string interpolation to customize the invitation for Ron and any other future Weasleys.

```python
>>>print weasley_invitation("Ron","Sunday", "May", "18th" )
The family of Ron Weasley proudly invite you to celebrate their graduation from Hogwarts on Sunday the May of 18th. Festivities will be held at The Burrow. See you then!

```

## Challenge 2 - The Guest List
Write a function, `invitee_name()` that turns Ron's friend's names into shortened names for the envelopes. The function should remove any nicknames (which Ron writes by surrounding them in single quotes) and return the first initial and last name of each guest.

```python
>>>print invitee_name("Hermione Granger")
H. Granger
>>>print invitee_name("Alstor 'Mad-Eye' Moody")
A. Moody
```

To remove the single quotes, you will have to use regular expressions. Whenever we use regular expressions, you must import the 're' package into your Python script. Then you preface the pattern you want to match with the letter `r`.
`.` - the dot stands for any character
`+`- the plus sign will include anything after that character

For example, to search for anything between `<` and `>`, use `<.+>`
```python
my_string="This <could be> the year that the Cubs win it all"
new_string=re.sub(r"<.+>","is",my_string)
```
This looks for any string that starts with a `<` and ends with a `>` and replaces it with the string `is`.

## Challenge 3 - Putting it all Together
Most of Ron's work is done, now just write a final function, `create_invitation()` that takes two arguments, one for the guest's name and one for the invitation message. The guest's name should be complete capitalized and followed by a comma. After a line break, the invitation's message should be printed.

```python
>>>print create_invitation(invitee_name("Alstor 'Mad-Eye' Moody"), weasley_invitation("Ron","Sunday", "May", "18th" ))
A. MOODY,
The family of Ron Weasley proudly invite you to celebrate their graduation from Hogwarts on Sunday the May of 18th. Festivities will be held at The Burrow. See you then!
```
