import wikipedia


user_input = raw_input("What would you like to learn about today? ")

print wikipedia.summary(user_input)
