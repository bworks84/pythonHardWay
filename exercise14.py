from sys import argv

script, user_name = argv
prompt = "> "

# again, enter arguments when running the python3 command
print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)
