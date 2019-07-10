greeting = input('Enter your name: ')
print('Hello'+' '+greeting+'!')


import datetime

time = datetime.datetime.now()
print('The current date and time is: ')
print(time)

while True:
    day = input('Are you ready to learn?: ')
    if day == "Yes":
        print('Let us begin!')

    elif day == "No":
        print('Too bad, let us begin!')

    elif day != 'Yes':
        print('Please enter Yes or No.')

    elif day != 'No':
        print('Please enter Yes or No.')
        break