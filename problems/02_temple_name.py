letter = ''' Dear <|Name|>,
You are selected! Greeting from ABC coding house, I am happy to tell you about your selection 
Have a great day ahead.
date: <|Date|>
'''
name = input("Enter your name: ")
date = input("Enter the date: ")
letter = letter.replace("<|Name|>", name)  # must go through this phase
letter = letter.replace("<|Date|>", date)  # must go through this phase
print(letter)
