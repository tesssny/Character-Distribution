"""
distribution.py
Author: tess snyder
Credit: http://www.tutorialspoint.com/python/python_tuples.htm, http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/, Mary feyrer, http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python, http://stackoverflow.com/questions/5212870/sorting-a-python-list-by-two-criteria

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
text=input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "'+text+'" is:')

text=text.lower()

import string

a=string.ascii_lowercase

countlist=[]

for x in a:
    number=text.count(x)
    if number>0: 
        countlist.append((x,number))

countlist = sorted(countlist, key=lambda x: (-x[1], x[0]))


for x in countlist:
    print(x[1]*x[0])
        


