# present the menu to the costumer

from operator import truediv

menu = {'latte': 185 , '3in1 coffee': 20 , 'americano' : 89, 'macchiato' : 135, 'regular-tea' : 80}


print( 'please choose from our available menu')
for key, value in menu.items():
    print(f'{key}: {value}')

def order():

    order = {}

    while True:

         order = input('can i take your order? (if you have no other order, type done) ')

         if order == 'done':
                break
         elif order in menu:
            pass
         else:
            print('the order is not in the menu, please try again (perhaps try to correct your spelling?')
    return order

def order_summary(order):
    if not order:
        print('you have no items ordered ')
        return
    print('Enjoy your order ')
    total = 0
    for key, value in order.item():
        item_total = menu[value]
        total += item_total
        print('your total is: ', total)


def main():
    order()
    order_summary(order)

main()





        





