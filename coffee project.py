# greet the user
print("hello, welcome to our cafe")

#ask the user if they want to order

while True:
    answer = input('do you want a coffee?: (yes/no) ')

    if answer == 'yes' :
        pass
        order = input('what coffee would you want to order: (small, medium, large) ')
        print('here is your ', order ,' coffee')
        break
    elif answer == 'no':
        print('understandable, have a great day')
        break
    else:
        print('im sorry, please correct your spelling')

# say goodbye to the user

print('thank you, please come again')

