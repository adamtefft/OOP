import InsectClass as I

mosquito = I.Insect('mosquito', 2, 4)
housefly = I.Insect('housefly', 2, 4)

mosquito.flight_length()
housefly.flight_length()

print(f"The {mosquito.get_name()} can fly up to {mosquito.get_miles()} miles")
print(f"The {housefly.get_name()} can fly up to {housefly.get_miles()} miles")


def main():
    my_insect = I.Insect()

    my_insect.flight_length()

    print(my_insect.get_flight())


main()
