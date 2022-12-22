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

        if order_item == "quit":
            break

        order_item = order_item.lower().title()

        if order_item == "Cart":
            print('Cart:')
            for item in menu_dict:
                if menu_dict[item] > 0:
                    print(f"{item}: {menu_dict[item]}")
        elif order_item not in menu_dict:
            print('Sorry, please pick from our menu.')
        else:
            menu_dict[order_item] += 1
            print(f"{menu_dict[order_item]} orders of {order_item} have been added.  See cart by typing 'cart'")

    print(farewell)


if __name__ == "__main__":
    main()
