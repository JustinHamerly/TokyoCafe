from textwrap import dedent

menu_dict = {
    "Fried Tofu": 0,
    "Edamame": 0,
    "Seasoned Cucumber": 0,
    "Pickled Ginger": 0,
    "Udon Noodles": 0,
    "Mushroom Ramen": 0,
    "Nori Rolls": 0,
    "Mochi Ice Cream": 0,
    "Fluffy Pancake": 0,
    "Daifuku": 0,
    "Black Tea": 0,
    "Boba Tea": 0,
    "Coffee": 0
}

greeting = dedent(
    """
    ****************************
    |  Welcome to Tokyo Cafe!  |
    ****************************
    
        to quit, type "quit"

    """
)

menu = dedent(
    """
    ****************************
    |           MENU           |
    ****************************
    
    APPETIZERS
    ----------------------------
    {}
    {}
    {}
    {}
    
    ENTREES
    ----------------------------
    {}
    {}
    {}
    
    DESSERT
    ----------------------------
    {}
    {}
    {}
    
    DRINKS
    ----------------------------
    {}
    {}
    {}
    
    """.format(*menu_dict)
)

order_prompt = dedent(
    '''
    ----------------------------
        What would you like?
    ----------------------------
    Type the food you would like
    Type 'help' for assistance
    '''
)

help_menu = dedent(
    '''
    Commands:
    cart - view your cart
    menu - view the menu
    clear - to clear your cart
    quit - to leave the app
    '''
)

farewell = dedent(
    """
    ****************************
    |        THANK YOU!        |
    ****************************
    """
)


def main():
    print(greeting)
    print(menu)

    while True:

        order_item = input(order_prompt)

        order_item = order_item.lower().title()

        if order_item == "Cart":
            print('Cart:')
            for item in menu_dict:
                if menu_dict[item] > 0:
                    print(f"{item}: {menu_dict[item]}")
        elif order_item == "Menu":
            print(menu)
        elif order_item == "Help":
            print(help_menu)
        elif order_item == "Clear":
            for item in menu_dict:
                menu_dict[item] = 0
        elif order_item == "Quit":
            break
        elif order_item not in menu_dict:
            print('Sorry, please pick from our menu.')
        else:
            menu_dict[order_item] += 1
            print(f"{menu_dict[order_item]} orders of {order_item} have been added.  See cart by typing 'cart'")

    print(farewell)


if __name__ == "__main__":
    main()
