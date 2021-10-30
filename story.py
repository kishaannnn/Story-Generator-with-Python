import random

opt = random.choice

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan', 'The other day', 'Many moons ago', 'About a fortnight ago']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat', 'a chinchilla with 3 eyes']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print( f"{opt(when)}, {opt(who)} called {opt(name)} that lived in {opt(residence)}, went to the {opt(went)} and {opt(happened)}" )
