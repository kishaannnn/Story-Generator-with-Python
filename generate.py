import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle']
name = ['Ali', 'Miriam', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'school', 'laundry']
happened = ['made a lot of friends', 'found a secret key', 'solved a mistery', 'wrote a book']

print( random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
