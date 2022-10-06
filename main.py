#Write pseudocode for a program that prompts a user to enter their name. If the name is “Hazel” then output “Hello Hazel”.  If the name is not Hazel, output “We haven’t met, ” name, “ pleased to meet you.” 
name = input('Enter your name: ')
if name == 'Hazel':
  print('Hello Hazel')
else:
  print(f'We haven't met {name}, pleased to meet you.')
