import CoinClass as c
# you are importing the name of the file, not of the class
# the "as c" lets you refer to "CoinClass" as "c"

# The main function.


def main():
    # Create an object from the Coin class.
    # my_coin is an instance
    # "Coin" is matching the name of the class
    # every time you want to make an instance, you would use c.Coin()
    my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

    # Display the side of the coin that is facing up.
    # notice you do not have to supply the argument/parameter
    print('This side is up:', my_coin.get_sideup())
    # you have to use the instance (in this case "my_coin") to access the files)

    # Toss the coin.
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()

        # Display the side of the coin that is facing up.
        print('This side is up:', my_coin.get_sideup())


# Call the main function.
main()
